
import json
import paho.mqtt.client as paho
from paho import mqtt
import time

def load_config(config_file):
    try:
        with open(config_file, 'r') as file:
            config = json.load(file)
        return config
    except Exception as e:
        raise

def get_data(data_file):
    try:
        with open(data_file, 'r') as file:
            config = json.load(file)
        return config
    except Exception as e:
        raise
     
def on_publish(client, userdata, mid, properties=None):
    print("mid: " + str(mid))

def main():
    config_file = 'config.json'
    data_file = 'mqtt_data.json'
    config = load_config(config_file)
    data = get_data(data_file)
    client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
    client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
    client.username_pw_set(username=config['username'], password=config['password'])
    client.connect(config['broker_url'], config['broker_port'], 60)
    client.on_publish = on_publish
    while 1:
        for item in data["data"]:
                client.publish(config['publish_url'], payload=str(item), qos=0)
                time.sleep(0.2)
if __name__ == "__main__":
    main()

