import paho.mqtt.client as mqtt
import time
import random

# ==== ThingSpeak MQTT Credentials ====
channel_id = "2894190" 
mqtt_client_id = "EwsuAikdLREfJhg4ER8bKSc"
mqtt_username = "EwsuAikdLREfJhg4ER8bKSc"
mqtt_password = "j0MZl6dFr34hIL/Pg9Mnzhyy"

# ==== MQTT Broker Settings ====
broker = "mqtt3.thingspeak.com"
port = 1883
topic = f"channels/{channel_id}/publish"

# ==== MQTT Setup ====
client = mqtt.Client(mqtt_client_id)
client.username_pw_set(mqtt_username, mqtt_password)
client.connect(broker, port, 60)

# ==== Data Publishing Loop ====
while True:
    # Generate random sensor data
    temperature = round(random.uniform(-10, 40), 2)
    humidity = round(random.uniform(30, 90), 2)
    co2 = round(random.uniform(400, 1800), 2)

    # Format payload for ThingSpeak
    payload = f"field1={temperature}&field2={humidity}&field3={co2}"

    # Publish to ThingSpeak
    client.publish(topic, payload)
    print(f"Published to ThingSpeak: {payload}")

    # ThingSpeak free tier requires at least 15s between updates
    time.sleep(15)
