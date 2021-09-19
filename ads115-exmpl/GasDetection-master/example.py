"""Example for gas detection module."""

import time
from gas_detection import GasDetection
import json
import paho.mqtt.client as mqtt


temp_pub_topic = "kichen/sensors/gas/MQ2"

def getPPM(ppm, detection):
    payload=json.dumps(
    {   "CO": ppm[detection.CO_GAS],
        "H2": ppm[detection.H2_GAS],
        "CH4":   ppm[detection.CH4_GAS],
        "LPG": ppm[detection.LPG_GAS],
        "PROPHANE": ppm[detection.PROPANE_GAS],
        "ALCOHOL":   ppm[detection.ALCOHOL_GAS],
        "SMOKE": ppm[detection.SMOKE_GAS]
    }
    )
    
    print(payload)
    return payload


def createMQTTClient():
  Broker = "192.168.1.151"
  hum_pub_topic = "living_room/weather/humidity"
  
  
  def on_connect(client, userdata, flags, rc):
      print("Connected with result code "+str(rc))
  
  def on_message(client, userdata, msg):
      message = str(msg.payload)
      print(msg.topic+" "+message)
  
  def on_publish(mosq, obj, mid):
      print(mosq)
  
  client = mqtt.Client()
  client.on_connect = on_connect
  client.on_message = on_message
  client.on_publish = on_publish
  
  client.connect(Broker, 1883, 60);
  return client



def main():
    """Handle example."""
    client = createMQTTClient()
    client.loop_start()

    print('Calibrating ...')
    detection = GasDetection()

    try:
        while True:
            ppm = detection.percentage()
            payload = getPPM(ppm, detection)
            client.publish(temp_pub_topic, payload)
            time.sleep(5)

    except KeyboardInterrupt:
        print('\nAborted by user!')

if __name__ == '__main__':
    main()
