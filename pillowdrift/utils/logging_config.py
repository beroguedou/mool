import os
import sys
import logging
from pathlib import Path

# Configure location for logs
BASE_DIR = Path(__file__).resolve().parent.parent.parent
LOGS_DIR = Path(BASE_DIR, 'logs')
LOGS_DIR.mkdir(parents=True, exist_ok=True)

# Logger
logging_config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'minimal': {'format': '%(message)s'},
        'detailed': {
            'format': '%(levelname)s %(asctime)s [%(filename)s:%(funcName)s:%(lineno)d]\n%(message)s\n'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
            'formatter': 'detailed',
            'level': logging.DEBUG,
        },
        'above-info': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': Path(LOGS_DIR, 'above-info.log'),
            'maxBytes': 10485760,  # 1 MB
            'backupCount': 10,
            'formatter': 'detailed',
            'level': logging.INFO,
        }
    },
    'loggers': {
        'root': {
            'handlers': ['console', 'above-info'],
            'level': logging.INFO,
            'propagate': True,
        },
    },
}
