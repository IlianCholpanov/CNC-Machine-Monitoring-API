from datetime import datetime
import random

class Machine:
    def __init__(self, machine_id):
        self.id = machine_id
        self.status = "STOP"
        self.start_time = None
        self.produced_parts = 0
        self.temperature = 25.5
        self.speed = 0.0
        self.water_level = 100
        self.waste_capacity = 0
        self.last_update = datetime.now()

    def update_readings(self):
        if self.status == "RUN":
            self.temperature += random.uniform(-0.5,1.5)
            self.speed = random.uniform(500, 3000)
            self.water_level = max(0.0, self.water_level - random.uniform(0,0.1))
            self.waste_capacity = min(100.0, self.waste_capacity + random.uniform(0, 0.02))
            if random.random() < 0.02:
                self.produced_parts += 1
        else:
            self.speed = 0

        self.last_update = datetime.now()

    def get_live_status(self):
        self.update_readings()
        return {
            "machine_id": self.id,
            "status": self.status,
            "temperature": round(self.temperature, 2),
            "speed": round(self.speed, 1),
            "water_level": round(self.water_level, 1),
            "waste_capacity": round(self.water_level, 1),
            "produced_parts": self.produced_parts,
            "timestamp": self.last_update.isoformat()
        }

    def start(self):
        self.status = "RUN"
        self.start_time = datetime.now()

    def stop(self):
        self.status = "STOP"