"""
    Configuration variables
"""

import json
import configparser
import os
import __root__

# Properties file
CONFIGURATION_FILE = os.path.join(__root__.path()+"/config/settings.conf")
# Config file parser
parser = configparser.RawConfigParser()

parser.read(CONFIGURATION_FILE)

# Service host
service_host = parser.get("SERVICE", "service_host")

# Service port number
service_port = int(parser.get("SERVICE", "service_port"))

# Database properties
DATABASE_NAME = parser.get('DATABASE', 'database_name')
DATABASE_HOST = parser.get('DATABASE', 'database_host')
DATABASE_PORT = parser.get('DATABASE', 'database_port')
DATABASE_USER = parser.get('DATABASE', 'database_user')
DATABASE_PASSWORD = parser.get('DATABASE', 'database_password')

# Log
LOG_BASE_PATH = parser.get('LOG', 'base_path')
LOG_LEVEL = parser.get('LOG', 'log_level')
FILE_NAME = LOG_BASE_PATH + parser.get('LOG', 'file_name')
LOG_HANDLERS = json.loads(parser.get('LOG', 'handlers'))
