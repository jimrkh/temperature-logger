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

# Humidity sensor DHT
HUMIDITY_SENSOR_DHT_PIN = 2
HUMIDITY_SENSOR_DHT_TYPE = "2302"

# Humidity sensor DHT
HUMIDITY_SENSOR_RAW1WIRE_ID = ""
HUMIDITY_SENSOR_RAW1WIRE_PATH_TEMPLATE = "/sys/bus/w1/devices/10-{}/w1_slave"


try:
    from config_local import *
except ImportError:
    raise ValueError("Please, provide local configuration file named 'config_local.py'.")
