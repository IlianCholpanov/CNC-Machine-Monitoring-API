from fastapi import FastAPI
from backend.models import Machine
from backend.data_logger import DataLogger

app = FastAPI(title="CNC Real-Time API")

# Инициализация
logger = DataLogger()
machines = {
    "M01": Machine("M01"),
    "M02": Machine("M02"),
    "M03": Machine("M03"),
    "M04": Machine("M04"),
}

@app.get("/machines")
def list_machines():
    return [{"machine_id": m.id, "status": m.status} for m in machines.values()]

@app.get("/machines/{machine_id}/live")
def live_status(machine_id: str):
    machine = machines[machine_id]
    data = machine.get_live_status()
    # логваме snapshot
    logger.update_machine_snapshot(machine)
    return data

@app.post("/machines/{machine_id}/start")
def start_machine(machine_id: str):
    machine = machines[machine_id]
    machine.start()
    logger.log_event(machine_id, "status_change", value=1, reason="start")
    logger.update_machine_snapshot(machine)
    return {"message": f"{machine_id} started"}

@app.post("/machines/{machine_id}/stop")
def stop_machine(machine_id: str, reason: str = "manual"):
    machine = machines[machine_id]
    machine.stop()
    logger.log_event(machine_id, "status_change", value=0, reason=reason)
    logger.update_machine_snapshot(machine)
    return {"message": f"{machine_id} stopped ({reason})"}

@app.post("/machines/{machine_id}/produce")
def produce_part(machine_id: str):
    machine = machines[machine_id]
    machine.produced_parts += 1
    logger.log_event(machine_id, "produced_part", value=1)
    logger.update_machine_snapshot(machine)
    return {"message": f"{machine_id} produced 1 part"}

@app.get("/machines/{machine_id}/summary")
def get_summary(machine_id: str):
    conn = logger.conn
    cursor = conn.execute("SELECT FROM machines WHERE machine_id=?", (machine_id,))
    row = cursor.fetchone()
    if row:
        return {
            "machine_id": row[0],
            "status": row[1],
            "temperature": row[2],
            "speed": row[3],
            "water_level": row[4],
            "waste_capacity": row[5],
            "produced_parts": row[6],
            "last_update": row[7]
        }
    else:
        return {"error": "Machine not found"}
