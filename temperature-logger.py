# -*- coding: utf-8 -*-

from w1thermsensor import W1ThermSensor
from config import (
    DB_HOST
)


def main():
    for sensor in W1ThermSensor.get_available_sensors():
        print("Sensor %s has temperature %.2f" % (sensor.id, sensor.get_temperature()))


if __name__ == "__main__":
    main()

