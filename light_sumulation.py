import paho.mqtt.client as mqtt
import time

broker_address = "157.173.101.159"
broker_port = 1883
topic = "/student_group/light_control"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
        print(f"Client state is {client._state}")
        client.subscribe(topic)
        print(f"Subscribed to topic: {topic}")
    else:
        print(f"Failed to connect, return code {rc}")

def on_message(client, userdata, msg):
    message = msg.payload.decode()
    print(f"Received message on topic {msg.topic}: {message}")
    if message == "ON":
        print("💡 Light is TURNED ON")
    elif message == "OFF":
        print("💡 Light is TURNED OFF")
    else:
        print(f"Unknown command received: {message}")

def on_subscribe(client, userdata, mid, granted_qos):
    print(f"Subscription confirmed")

client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message
client.on_subscribe = on_subscribe

print(f"Connecting to broker...")
client.connect(broker_address, broker_port, 60)

client.loop_start()

try:
    print("Light Simulation Running...")
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Disconnecting from broker")
    client.disconnect()
    client.loop_stop()