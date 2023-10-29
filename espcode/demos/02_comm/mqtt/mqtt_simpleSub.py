import time
from umqtt.simple import MQTTClient

from customnetwork import customnetwork
customnetwork.start()

# publish test messages:
# mosquitto_pub -h broker.hivemq.com -t iot_simple_sub -m 'hello'

# received messages from subscriptions will be delivered to this callback
def subCallback(topic, msg):
    print((topic, msg))

def main(server = "broker.hivemq.com"):
    c = MQTTClient("umqtt_client", server)
    c.set_callback(subCallback)
    c.connect()
    c.subscribe(b"iot_simple_sub")
    try:
        while True:
            if True:
                # Blocking wait for message
                c.wait_msg()
            else:
                # Non-blocking wait for message
                c.check_msg()
                # Then need to sleep to avoid 100% CPU usage (in a real
                # app other useful actions would be performed instead)
                time.sleep(1)
    finally:
        c.disconnect()

if __name__ == "__main__":
    main()
