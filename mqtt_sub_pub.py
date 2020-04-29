import paho.mqtt.client as mqtt
import numpy as np
from scipy.fftpack import fft
import ast

# The callback for when the client receives a CONNACK response from the server.


def on_publish(client, userdata, result):  # create function for callback
    pass


def on_connect(client, userdata, flags, rc):
    # print("Connected with result code "+str(rc))
    client.subscribe("motor1/imuTemp")

# The callback for when a PUBLISH message is received from the server.


def on_message(client, userdata, msg):
    raw = (ast.literal_eval(str(msg.payload.decode())))
    # print(len(raw))
    fftTf = fft(raw)

    for ftt in abs(fftTf):
        sensor_data['vibration_fft'] = fft
        # topic: v1/devices/me/telemetry
        ret = client1.publish("v1/devices/me/telemetry",
                              json.dumps(sensor_data))

    # client.publish('m0/fft',str(abs(fftTf)))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set("USERNAME", password="PWD")
client.connect("IP", 1885, 60)


# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
ACCESS_TOKEN = 'B1_TEST_TOKEN'  # Token of your device
broker = "IP"  # host name
port = 1883
client1 = mqtt.Client("control1")  # create client object
client1.on_publish = on_publish  # assign function to callback
client1.username_pw_set(ACCESS_TOKEN)  # access token from thingsboard device
client1.connect(broker, port, keepalive=60)  # establish connection
sensor_data = {'vibration_fft': 0}

client.loop_forever()
