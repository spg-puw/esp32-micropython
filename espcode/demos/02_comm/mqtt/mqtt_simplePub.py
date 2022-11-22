from umqtt.simple import MQTTClient
import customnetwork
customnetwork.setupSTA()

# Test reception e.g. with:
# mosquitto_sub -t foo_topic


def main(server="192.189.51.159"):
    c = MQTTClient("umqtt_client", server)
    c.connect()
    c.publish(b"foo_topic", b"hello")
    c.disconnect()


if __name__ == "__main__":
    main()