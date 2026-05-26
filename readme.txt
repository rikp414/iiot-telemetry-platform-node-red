# Project 2.0 — IIoT Telemetry Pipeline Using Node-RED

## Overview

Project 2.0 is a simulated Industrial IoT (IIoT) telemetry system built using Python, MQTT, Mosquitto, Node-RED, SQLite, and Dashboard visualization.

The system simulates industrial machine telemetry, publishes data through MQTT, processes and cleans telemetry inside Node-RED middleware, stores historical telemetry in SQLite, and visualizes live machine data on a dashboard.

---

# Technologies Used

- Python
- MQTT
- Mosquitto Broker
- Node-RED
- SQLite
- Node-RED Dashboard

---

# Features

- Random telemetry generation
- Nested JSON payload processing
- MQTT publish/subscribe communication
- Telemetry validation
- Data cleaning and normalization
- Historical telemetry storage
- Live dashboard monitoring
- Multi-line telemetry charts
- Machine state visualization

---

# System Architecture

```text
+-----------------------+
| Python Gateway        |
| Telemetry Simulator   |
+-----------------------+
           |
           | MQTT Publish
           v
+-----------------------+
| Mosquitto MQTT Broker |
+-----------------------+
           |
           | MQTT Subscribe
           v
+-----------------------+
| Node-RED Middleware   |
|-----------------------|
| JSON Parsing          |
| Validation Layer      |
| Cleaning Layer        |
| SQL Insert Builder    |
+-----------------------+
           |
           v
+-----------------------+
| SQLite Database       |
| telemetry.db          |
+-----------------------+
           |
           v
+------------------------+
| Dashboard Visualization|
|------------------------|
| Temperature Gauge      |
| RPM Gauge              |
| Machine State          |
| Telemetry Charts       |
+------------------------+
```

---

# Telemetry Flow

```text
Gateway
   ↓
MQTT Broker
   ↓
Node-RED Middleware
   ↓
Validation
   ↓
Cleaning / Normalization
   ↓
SQLite Historian
   ↓
Dashboard Visualization
```

---

# Dashboard Components

- Temperature Gauge
- RPM Gauge
- Machine State Display
- Location Display
- Live Telemetry Trend Charts

---

# Database

Telemetry data is stored inside:

```text
telemetry.db
```

Example telemetry fields:

- machine_id
- location
- temperature
- humidity
- pressure
- rpm
- vibration
- signal
- timestamp

---

# Learning Outcomes

This project demonstrates:

- MQTT communication
- IIoT telemetry pipelines
- Middleware engineering
- JSON processing
- Data normalization
- Historical telemetry storage
- Real-time dashboard visualization
- SCADA/IIoT architecture concepts

---

# Future Improvements

- REST API integration
- Multi-machine support
- Alarm system
- Predictive maintenance
- AI anomaly detection
- Cloud integration
- Grafana integration
- Custom frontend dashboard

