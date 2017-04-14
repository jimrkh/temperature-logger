# -*- coding: utf-8 -*-

# InfluxDB
INFLUXDB_HOST = 'localhost' 
INFLUXDB_PORT = 8086
INFLUXDB_DB = 'home'
INFLUXDB_NAME = ''
INFLUXDB_PASSWD = ''


try:
    from config_local import *
except ImportError:
    raise ValueError("Please, provide local configuration file named 'config_local.py'.")

