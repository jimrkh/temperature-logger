# -*- coding: utf-8 -*-

# InfluxDB
DB_HOST=''


try:
    from config_local import *
except ImportError:
    raise ValueError("Please, provide local configuration file named 'config_local.py'.")

