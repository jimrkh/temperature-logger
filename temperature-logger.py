# -*- coding: utf-8 -*-

import time
import schedule

from w1thermsensor import W1ThermSensor
from config import (
    INFLUXDB_HOST, INFLUXDB_PORT, INFLUXDB_DB, INFLUXDB_NAME, INFLUXDB_PASSWD
)


def job():
    for sensor in W1ThermSensor.get_available_sensors():
        print("Sensor %s has temperature %.2f at %s" % (sensor.id, sensor.get_temperature(), time.time()))


def main():
    schedule.every(1).minutes.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()

