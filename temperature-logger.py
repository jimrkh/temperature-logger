# -*- coding: utf-8 -*-

import schedule

from w1thermsensor import W1ThermSensor
from config import (
    DB_HOST
)


def job():
    for sensor in W1ThermSensor.get_available_sensors():
        print("Sensor %s has temperature %.2f" % (sensor.id, sensor.get_temperature()))


def main():
    schedule.every(1).minutes.do(job)
    while True:
        schedule.run_pending()

if __name__ == "__main__":
    main()
