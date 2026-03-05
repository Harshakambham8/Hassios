import sqlite3
from datetime import datetime

DB_PATH = "database/hassios.db"

def log_work(intent=None, project=None, hours=None, **kwargs):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS work_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project TEXT,
            hours REAL,
            timestamp TEXT
        )
    """)

    cursor.execute("""
        INSERT INTO work_logs (project, hours, timestamp)
        VALUES (?, ?, ?)
    """, (project, hours, datetime.now().isoformat()))

    conn.commit()
    conn.close()

    return f"Logged {hours} hours for {project}."
