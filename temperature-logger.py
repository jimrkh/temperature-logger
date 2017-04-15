# -*- coding: utf-8 -*-

import time
from datetime import datetime

import schedule
from influxdb import InfluxDBClient
from w1thermsensor import W1ThermSensor

from config import (
    SCHEDULE_TIME_DELTA,
    INFLUXDB_HOST, INFLUXDB_PORT, INFLUXDB_DB, INFLUXDB_NAME, INFLUXDB_PASSWD,
    SENSOR_LOCATIONS_NA, SENSOR_LOCATIONS
)


def job():
    measurement_list = []

    for sensor in W1ThermSensor.get_available_sensors():
        measurement_value = sensor.get_temperature(W1ThermSensor.DEGREES_C)
        measurement_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

        measurement = {
            "measurement": "temperature_sensor",
            "tags": {
                "id": sensor.id,
                # "prefix": sensor.slave_prefix,
                # "path": sensor.sensorpath,
                "device_name": sensor.type_name,
                "device_type": sensor.type,
                "location": SENSOR_LOCATIONS.get(sensor.id,SENSOR_LOCATIONS_NA),
                "unit": "C",
            },
            "time": measurement_time,
            "fields": {
                "value": measurement_value,
            },
        }
        print("Sensor %s has temperature %.2f at %s" % (sensor.id, measurement_value, measurement_time))
        measurement_list.append(measurement)

    db_client = InfluxDBClient(INFLUXDB_HOST, INFLUXDB_PORT, INFLUXDB_NAME, INFLUXDB_PASSWD, INFLUXDB_DB)
    db_client.write_points(measurement_list)


def main():
    schedule.every(SCHEDULE_TIME_DELTA).seconds.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
