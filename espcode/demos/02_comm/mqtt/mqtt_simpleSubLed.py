import machine
from umqtt.simple import MQTTClient

from customnetwork import customnetwork
customnetwork.start()

# publish test messages:
# mosquitto_pub -h broker.hivemq.com -t iot_led -m 'toggle'

ledIntern = machine.Pin(2, machine.Pin.OUT, value=1)
topic = b"iot_led"

state = 0

def subCallback(topic, msg):
    global state
    print((topic, msg))
    if msg == b"on":
        ledIntern.value(0)
        state = 1
    elif msg == b"off":
        ledIntern.value(1)
        state = 0
    elif msg == b"toggle":
        ledIntern.value(state)
        state = 1 - state
    else:
        print("unknown message")

def main(server = "broker.hivemq.com"):
    c = MQTTClient("umqtt_client", server)
    c.set_callback(subCallback)
    c.connect()
    c.subscribe(topic)
    print("Connected to {0}, subscribed to topic {1}".format(server, topic))
    try:
        while True:
            # micropython.mem_info()
            c.wait_msg()
    finally:
        c.disconnect()

if __name__ == "__main__":
    main()