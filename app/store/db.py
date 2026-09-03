"""SQLite index over the file outputs. See docs/decisions/0002.

Not a business output: every column is derivable from an artifact on disk, so
deleting the file and rescanning `result/` must reproduce it exactly.
"""

import sqlite3
from pathlib import Path

from app import config
from app.config import rel_to_root

SCHEMA_VERSION = 2

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

CREATE TABLE IF NOT EXISTS downloads (
    package_name TEXT PRIMARY KEY,
    source       TEXT,                   -- which adapter served it
    state        TEXT NOT NULL,          -- queued | fetching | verifying | ready | failed
    file_path    TEXT,
    version      TEXT,
    requested_at TEXT NOT NULL,
    error        TEXT
);

CREATE INDEX IF NOT EXISTS idx_apps_run     ON apps(run_id);
CREATE INDEX IF NOT EXISTS idx_apps_package ON apps(package_name);
CREATE INDEX IF NOT EXISTS idx_artifacts_app ON artifacts(app_id);
"""


_TABLES = ("artifacts", "apps", "downloads", "runs")   # children first


def connect() -> sqlite3.Connection:
    """Open (creating if needed) and bring the schema up to date."""
    # Read HERE, not bound at import: the tests redirect it through MA_DB_PATH.
    db_path = config.DB_PATH
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    # WAL so a reader never blocks the writer, the normal state during a batch.
    conn.execute("PRAGMA journal_mode = WAL")
    _migrate(conn)
    conn.executescript(_SCHEMA)
    return conn


def _migrate(conn: sqlite3.Connection) -> None:
    """Schema changes are applied by REBUILDING, not by ALTER.

    `CREATE TABLE IF NOT EXISTS` silently does nothing when the table exists, so
    adding a column without this leaves an old database missing it and every
    query failing at runtime. Callers re-populate with store.index.rescan().
    """
    current = conn.execute("PRAGMA user_version").fetchone()[0]
    if current == SCHEMA_VERSION:
        return
    for table in _TABLES:
        conn.execute(f"DROP TABLE IF EXISTS {table}")
    conn.execute(f"PRAGMA user_version = {SCHEMA_VERSION}")
    conn.commit()


# Relative to the repo root; absolute paths do not travel. One implementation,
# in config, so the index and the API cannot disagree.
rel = rel_to_root
