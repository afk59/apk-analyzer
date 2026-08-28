"""SQLite index over the file outputs. See docs/decisions/0002.

The database is NOT a business output. Every column here is derivable from an
artifact on disk, so deleting the file and rescanning `result/` must reproduce
it exactly. Nothing may be shown to a user that exists only in this file.
"""

import sqlite3
from pathlib import Path

from app.config import DB_PATH, rel_to_root

SCHEMA_VERSION = 1

_SCHEMA = """
CREATE TABLE IF NOT EXISTS runs (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    started_at   TEXT NOT NULL,
    finished_at  TEXT,
    mode         TEXT NOT NULL,          -- single | batch | download
    target       TEXT NOT NULL,          -- hmos | hms
    status       TEXT NOT NULL,          -- running | done | failed | cancelled
    input_path   TEXT NOT NULL,
    file_count   INTEGER NOT NULL DEFAULT 0
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


def connect() -> sqlite3.Connection:
    """Open (creating if needed) and bring the schema up to date."""
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    # WAL so a reader (the UI listing results) never blocks the writer (a worker
    # finishing a file), which is the normal state during a batch.
    conn.execute("PRAGMA journal_mode = WAL")
    conn.executescript(_SCHEMA)
    _migrate(conn)
    return conn


def _migrate(conn: sqlite3.Connection) -> None:
    """Forward-only migrations, keyed on PRAGMA user_version.

    The safety net for a wrong migration is that this file is disposable:
    delete it and rescan. That is only true while the rule in the module
    docstring holds, so it is worth re-reading before adding a column.
    """
    current = conn.execute("PRAGMA user_version").fetchone()[0]
    if current < SCHEMA_VERSION:
        conn.execute(f"PRAGMA user_version = {SCHEMA_VERSION}")
        conn.commit()


# Store paths relative to the repo root; absolute ones do not travel. One
# implementation, in config, so the index and the API can never disagree about
# what a stored path means.
rel = rel_to_root
