from umqtt.simple import MQTTClient
from customnetwork import customnetwork
customnetwork.start()

# test reception with:
# mosquitto_sub -h broker.hivemq.com -t 'some_iot_topic'

def main(server="broker.hivemq.com"):
    c = MQTTClient("umqtt_client", server)
    c.connect()
    c.publish(b"some_iot_topic", b"1234")
    c.disconnect()

if __name__ == "__main__":
    main()
