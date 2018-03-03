# -*- coding: utf-8 -*-

# Schedule
SCHEDULE_TIME_DELTA = 30  # in seconds (Minimum value 3 sec)

# InfluxDB
INFLUXDB_HOST = 'localhost' 
INFLUXDB_PORT = 8086
INFLUXDB_DB = 'home'
INFLUXDB_NAME = ''
INFLUXDB_PASSWD = ''

# Sensors
SENSOR_LOCATIONS_NA = "N/A"
SENSOR_LOCATIONS = {}  # key = sensor.id, value = <your sensor location name>

# Humidity sensor
HUMIDITY_SENSOR_PIN = 2
HUMIDITY_SENSOR_TYPE = "2302"


try:
    from config_local import *
except ImportError:
    raise ValueError("Please, provide local configuration file named 'config_local.py'.")
