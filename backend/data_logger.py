from backend.db import init_db
from datetime import datetime

class DataLogger:
    def __init__(self):
        self.conn = init_db()

    def log_event(self, machine_id, event_type, value=None, reason=None):
        query = "INSERT INTO events (machine_id, event_type, value, reason, timestamp) VALUES (?, ?, ?, ?, ?)"
        self.conn.execute(query, (machine_id, event_type, value, reason, datetime.now().isoformat()))
        self.conn.commit()

    def update_machine_snapshot(self, machine):
        query = """
        INSERT INTO machines (machine_id, status, temperature, speed, water_level, waste_capacity, produced_parts, last_update)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(machine_id) DO UPDATE SET
            status=excluded.status,
            temperature=excluded.temperature,
            speed=excluded.speed,
            water_level=excluded.water_level,
            waste_capacity=excluded.waste_capacity,
            produced_parts=excluded.produced_parts,
            last_update=excluded.last_update
        """
        self.conn.execute(query, (
            machine.id,
            machine.status,
            machine.temperature,
            machine.speed,
            machine.water_level,
            machine.waste_capacity,
            machine.produced_parts,
            machine.last_update.isoformat()
        ))
        self.conn.commit()
