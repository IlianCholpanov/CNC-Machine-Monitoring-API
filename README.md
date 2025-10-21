## CNC Machine Monitoring — Real-Time API & Dashboard

A Python-based simulation and monitoring system for CNC machines.
It provides real-time machine data through a FastAPI backend, logs all events in SQLite.

## 1️⃣ Overview

The project simulates a machine monitoring system for a CNC workshop.
Each machine generates real-time readings (temperature, speed, water level, waste capacity, etc.), which are served via REST API and stored in an SQLite database.

### **The app includes:** 

* Machine simulation (Machine class)

* REST API (FastAPI)

* Event & snapshot logging (SQLite via DataLogger)

* Extensible structure for real-time dashboard or hardware integration

## 2️⃣ Features

✅ Real-time machine data simulation\
✅ REST API for live data, control, and summary\
✅ Persistent event logging in SQLite\
✅ Automatic database initialization\
✅ Extendable to real-world machine sensors or WebSocket streaming


## 3️⃣ Project Architecture

```
machine_monitoring/
├── backend/
│   ├── __init__.py
│   ├── api.py            # FastAPI application (endpoints)
│   ├── data_logger.py    # Logs events & updates machine snapshots   
│   ├── db.py             # SQLite initialization and connection
│   └── models.py         # Machine simulation logic
├── data/
│   └── machine_data.db   # Created automatically
├── requirements.txt
└── README.md
```

## 4️⃣ Installation Guide
### **Step** 1 — Clone the repository
```bash
    git clone <your-repo-url> machine_monitoring
    cd machine_monitoring
```

### **Step**  2 — Create and activate a virtual environment
```bash
    python -m venv .venv
    
    # Windows
    .vevn/Scripts/Active.ps1
    
    # macOS / Linux
    source .venv/bin/activate
```

### **Step** 3 — Install dependencies
```bash
    pip install -r requirements.txt
```

## 5️⃣ How to Run
### ▶️ Run the FastAPI backend
```bash
    uvicorn backend.api:app --reload
```
