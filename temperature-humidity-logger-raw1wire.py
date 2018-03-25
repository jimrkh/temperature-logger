# -*- coding: utf-8 -*-

import time
from datetime import datetime

import schedule
from influxdb import InfluxDBClient

from config import (
    SCHEDULE_TIME_DELTA,
    INFLUXDB_HOST, INFLUXDB_PORT, INFLUXDB_DB, INFLUXDB_NAME, INFLUXDB_PASSWD,
    SENSOR_LOCATIONS_NA, SENSOR_LOCATIONS,
    HUMIDITY_SENSOR_RAW1WIRE_ID, HUMIDITY_SENSOR_RAW1WIRE_PATH_TEMPLATE
)


_SENSOR_TYPE = "raw1wire"


def _raw_sensor_value():
    sensor_path = HUMIDITY_SENSOR_RAW1WIRE_PATH_TEMPLATE.format(HUMIDITY_SENSOR_RAW1WIRE_ID)
    with open(sensor_path, "r") as f:
        lines = f.readlines()

    if lines[0].strip()[-3:] == "YES":
        data = lines[0].split(" ")
        temperature = float.fromhex(data[1] + data[0])
        humidity = float.fromhex(data[3] + data[2])
        return humidity, temperature

    return


def job():
    # Read temperature and humidity values from sensor
    humidity, temperature = _raw_sensor_value()

    measurement_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

    measurement = {
        "measurement": "temperature_humidity_sensor",
        "tags": {
            "device_id": HUMIDITY_SENSOR_RAW1WIRE_ID,
            "device_type": _SENSOR_TYPE,
            "location": SENSOR_LOCATIONS.get(HUMIDITY_SENSOR_RAW1WIRE_ID, SENSOR_LOCATIONS_NA),
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
        _SENSOR_TYPE, temperature, humidity, measurement_time
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
