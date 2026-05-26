import json
import random
import time
import paho.mqtt.client as mqtt

# -----------------------------
# MQTT CONFIG
# -----------------------------

BROKER = "localhost"
PORT = 1883

TOPIC = "factory/machine1/telemetry"

# -----------------------------
# MQTT CLIENT
# -----------------------------

client = mqtt.Client()

client.connect(BROKER, PORT, 60)

print("Connected to MQTT Broker")

# -----------------------------
# MAIN LOOP
# -----------------------------

while True:

    # Simulated telemetry
    payload = {

        "machine_id": "M1",

        "location": "Plant_A",

        "sensors": {

            # intentionally strings
            "temperature": str(round(random.uniform(20, 90), 2)),

            "humidity": str(random.randint(30, 80)),

            "pressure": str(round(random.uniform(1, 5), 2))
        },

        "motor": {

            "rpm": str(random.randint(1200, 1800)),

            "running": str(random.choice([True, False])).lower()
        },

        "network": {

            "signal": str(random.randint(60, 100))
        },

        "timestamp": time.time()
    }

    # Convert dictionary -> JSON
    json_payload = json.dumps(payload)

    # Publish MQTT
    client.publish(TOPIC, json_payload)

    print("\nPublished Telemetry:")
    print(json.dumps(payload, indent=2))

    # Wait 5 seconds
    time.sleep(5)