import time
import ubinascii
import machine
from umqtt.simple import MQTTClient

from customnetwork import customnetwork
customnetwork.start()

# test reception with:
# mosquitto_sub -h broker.hivemq.com -t 'iot_led'

button = machine.Pin(0, machine.Pin.IN)
serverDefault = "broker.hivemq.com"
clientId = ubinascii.hexlify(machine.unique_id())
topic = b"iot_led"

def main(server=serverDefault):
    c = MQTTClient(clientId, server)
    c.connect()
    print("connected to {0}, waiting for button presses".format(server))
    try:
        while True:
            while True:
                if button.value() == 0:
                    break
                time.sleep_ms(20)
            print("button pressed")
            c.publish(topic, b"toggle")
            time.sleep_ms(200)
    finally:
        c.disconnect()

if __name__ == "__main__":
    main()
