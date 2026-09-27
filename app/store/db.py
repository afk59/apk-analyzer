"""SQLite index over the file outputs. See docs/decisions/0002.

The database is NOT a business output. Every column here is derivable from an
artifact on disk, so deleting the file and rescanning `result/` must reproduce
it exactly. Nothing may be shown to a user that exists only in this file.
"""

import sqlite3
from pathlib import Path

from app import config
from app.config import rel_to_root

SCHEMA_VERSION = 3

_SCHEMA = """
CREATE TABLE IF NOT EXISTS runs (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    started_at   TEXT NOT NULL,
    finished_at  TEXT,
    mode         TEXT NOT NULL,          -- single | batch | download
    target       TEXT NOT NULL,          -- hmos | hms
    status       TEXT NOT NULL,          -- running | done | failed | cancelled
    input_path   TEXT NOT NULL,
    file_count   INTEGER NOT NULL DEFAULT 0,
    -- Files this run chose not to re-analyse because a report already existed.
    -- They belong to the run that PRODUCED them, so they are not listed here as
    -- apps -- but a run that skipped everything would otherwise read as "0 apps"
    -- and look like it did nothing.
    skipped_count INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS apps (
    id                INTEGER PRIMARY KEY AUTOINCREMENT,
    run_id            INTEGER NOT NULL REFERENCES runs(id) ON DELETE CASCADE,
    source_file       TEXT NOT NULL,
    package_name      TEXT,
    app_name          TEXT,
    version           TEXT,
    framework         TEXT,              -- "React Native", "Unknown", ...
    engine_name       TEXT,              -- Hermes | JSC | N/A
    packer            TEXT,              -- set only when the DEX is packed
    -- Straight from engine.core.renderer.coverage_status(). NEVER recomputed:
    -- that function is the one source of truth the report and the workbook
    -- already share, and a fourth implementation would let them disagree.
    coverage_pct      REAL,              -- NULL unless coverage_status == 'ok'
    coverage_status   TEXT,              -- ok | packed | low | none
    kit_count         INTEGER,
    unmapped_count    INTEGER,
    ohpm_count        INTEGER,
    permission_count  INTEGER,
    analysis_time_sec REAL,
    status            TEXT NOT NULL,     -- done | failed
    error             TEXT
);

CREATE TABLE IF NOT EXISTS artifacts (
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    app_id  INTEGER NOT NULL REFERENCES apps(id) ON DELETE CASCADE,
    kind    TEXT NOT NULL,               -- html | xlsx | agent_json
    -- Relative to the repo root, so a moved or shared checkout still resolves.
    path    TEXT NOT NULL
);

-- Where a downloaded binary came from (docs/decisions/0006). One row per
-- attempt, under the run that made it, so a result traces to its source even
-- after the same package is fetched again. Rebuilt from the run manifests.
CREATE TABLE IF NOT EXISTS downloads (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    run_id       INTEGER NOT NULL REFERENCES runs(id) ON DELETE CASCADE,
    package_name TEXT NOT NULL,
    source       TEXT,                   -- which adapter served it
    state        TEXT NOT NULL,          -- ready | not_found | failed
    file_path    TEXT,
    version      TEXT,                   -- versionName from the verified manifest
    size         INTEGER,
    requested_at TEXT NOT NULL,
    error        TEXT,
    note         TEXT                    -- e.g. config splits dropped from a bundle
);

CREATE INDEX IF NOT EXISTS idx_apps_run     ON apps(run_id);
CREATE INDEX IF NOT EXISTS idx_apps_package ON apps(package_name);
CREATE INDEX IF NOT EXISTS idx_artifacts_app ON artifacts(app_id);
CREATE INDEX IF NOT EXISTS idx_downloads_run ON downloads(run_id);
"""


_TABLES = ("artifacts", "apps", "downloads", "runs")   # children first


def connect() -> sqlite3.Connection:
    """Open (creating if needed) and bring the schema up to date."""
    # config.DB_PATH is read HERE, not bound at import: the test suite redirects
    # it through MA_DB_PATH, and an import-time binding would have every test
    # writing into the real database.
    db_path = config.DB_PATH
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    # WAL so a reader (the UI listing results) never blocks the writer (a worker
    # finishing a file), which is the normal state during a batch.
    conn.execute("PRAGMA journal_mode = WAL")
    _migrate(conn)
    conn.executescript(_SCHEMA)
    return conn


def _migrate(conn: sqlite3.Connection) -> None:
    """Schema changes are applied by REBUILDING, not by ALTER.

    This file is an index: every column in it is derivable from an artifact on
    disk (see the module docstring and docs/decisions/0002), so the correct
    response to a schema change is to throw the copy away and re-derive it. That
    is simpler than a migration ladder and it cannot leave a half-migrated
    database behind.

    It also avoids a trap: `CREATE TABLE IF NOT EXISTS` silently does nothing
    when the table exists, so adding a column to _SCHEMA without this would
    leave an old database missing that column and every query against it
    failing at runtime rather than at upgrade time.

    Callers re-populate by calling store.index.rescan(); /api/results does it
    automatically when it finds an empty index and reports on disk.
    """
    current = conn.execute("PRAGMA user_version").fetchone()[0]
    if current == SCHEMA_VERSION:
        return
    for table in _TABLES:
        conn.execute(f"DROP TABLE IF EXISTS {table}")
    conn.execute(f"PRAGMA user_version = {SCHEMA_VERSION}")
    conn.commit()


# Store paths relative to the repo root; absolute ones do not travel. One
# implementation, in config, so the index and the API can never disagree about
# what a stored path means.
rel = rel_to_root
