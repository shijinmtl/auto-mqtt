# MQTT Publisher Script

This script (`publish.py`) connects to an MQTT broker and publishes data from a JSON file to a specified topic.

## Prerequisites

Before running the script, ensure you have the following:

1. **Python 3.x**: Ensure Python 3.x is installed on your system.
2. **Paho MQTT Client Library**: This script uses the Paho MQTT client library. Install it using pip if you haven't already:

    ```bash
    pip install paho-mqtt
    ```

## Configuration

### `config.json`

Create a `config.json` file in the same directory as `publish.py` with the following structure:

```json
{
    "broker_url": "YOUR_BROKER_URL",
    "username": "YOUR_USERNAME",
    "password": "YOUR_PASSWORD",
    "broker_port": 8883,
    "publish_url": "YOUR_TOPIC"
}


##  Running script 

```bash
    python3 publish.py
    ```


This script will keep posting data to the mqtt brocker 