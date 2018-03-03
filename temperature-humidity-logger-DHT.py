# -*- coding: utf-8 -*-

import time
from datetime import datetime

import Adafruit_DHT
import schedule
from influxdb import InfluxDBClient

from config import (
    SCHEDULE_TIME_DELTA,
    INFLUXDB_HOST, INFLUXDB_PORT, INFLUXDB_DB, INFLUXDB_NAME, INFLUXDB_PASSWD,
    SENSOR_LOCATIONS_NA, SENSOR_LOCATIONS,
    HUMIDITY_SENSOR_PIN, HUMIDITY_SENSOR_TYPE
)


# Parse command line parameters.
_SENSOR_TYPES = {
    '11': Adafruit_DHT.DHT11,
    '22': Adafruit_DHT.DHT22,
    '2302': Adafruit_DHT.AM2302
}


def job():
    sensor_type = _SENSOR_TYPES[str(HUMIDITY_SENSOR_TYPE)]
    # Read temperature and humidity values from sensor
    humidity, temperature = Adafruit_DHT.read_retry(sensor_type, HUMIDITY_SENSOR_PIN)
    measurement_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

    measurement = {
        "measurement": "temperature_humidity_sensor",
        "tags": {
            "device_pin": HUMIDITY_SENSOR_PIN,
            "device_type": sensor_type,
            "location": SENSOR_LOCATIONS.get(
                "{}-{}".format(HUMIDITY_SENSOR_PIN, sensor_type), SENSOR_LOCATIONS_NA
            ),
            "temperature_unit": "C",
            "humidity_unit": "%",
        },
        "time": measurement_time,
        "fields": {
            "temperature_value": temperature,
            "humidity_value": humidity,
        },
    }
    print("Sensor %s has temperature %.2f, humidity %.2f at %s" % (
        sensor_type, temperature, humidity, measurement_time
    ))

    db_client = InfluxDBClient(INFLUXDB_HOST, INFLUXDB_PORT, INFLUXDB_NAME, INFLUXDB_PASSWD, INFLUXDB_DB)
    db_client.write_points([measurement])


def main():
    schedule.every(SCHEDULE_TIME_DELTA).seconds.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
