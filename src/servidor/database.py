import sqlite3 
from config import Config


def crear_db():
    conn = sqlite3.connect(Config.DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            received_at TEXT,
            service_name TEXT,
            severity TEXT,
            message TEXT
        )
    ''')
    conn.commit()
    conn.close()
    