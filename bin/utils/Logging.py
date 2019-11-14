"""
    Logging module
"""
import logging.handlers
import sys
from logging import StreamHandler

from bin.common import AppConfigurations as __AppConf

# File name
__LOG_FILE = __AppConf.FILE_NAME


# Log file handlers
__LOG_HANDLERS = __AppConf.LOG_HANDLERS

# Logger object is created
__logger = logging.getLogger("zs_Leave")

# Setting log level
__logger.setLevel(__AppConf.LOG_LEVEL)

# Logging format is set
__formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s  - %(filename)s - %(module)s: %(funcName)s: '
                                '%(lineno)d - %(message)s')

if 'file' in __LOG_HANDLERS:
    # Adding the log file handler to the logger
    __file_handler = logging.handlers.TimedRotatingFileHandler(__LOG_FILE)
    __file_handler.setFormatter(__formatter)
    __logger.addHandler(__file_handler)


if 'console' in __LOG_HANDLERS:
    # Adding the log Console handler to the logger
    __console_handler = StreamHandler(sys.stdout)
    __console_handler.setFormatter(__formatter)
    __logger.addHandler(__console_handler)


def get_logger():
    """
    Returns logger object
    :return:
    """
    return __logger
