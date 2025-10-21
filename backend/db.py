import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "../data/machine_data.db")

def get_connection():
    if not os.path.exists(os.path.dirname(DB_PATH)):
        os.makedirs(os.path.dirname(DB_PATH))
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    return conn


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS events (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       machine_id TEXT,
       event_type TEXT,
       value REAL,
       reason TEXT,
       timestamp TEXT
   )
   """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS machines (
       machine_id TEXT PRIMARY KEY,
       status TEXT,
       temperature REAL,
       speed REAL,
       water_level REAL,
       waste_capacity REAL,
       produced_parts INTEGER,
       last_update TEXT
    )
    """)

    conn.commit()
    return conn
