import logging
from logging.handlers import TimedRotatingFileHandler
import pathlib
import os
import sys
from unittest.mock import DEFAULT

from classification_model.config.config import FEATURES

PACKAGE_ROOT = pathlib.Path(__file__).resolve().parent.parent

FORMATTER = logging.Formatter(
    "%(asctime)s — %(name)s — %(levelname)s —"
    "%(funcName)s:%(lineno)d — %(message)s")
LOG_DIR = PACKAGE_ROOT / 'logs'
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / 'ml_api.log'

FEATURES = {'credit_score': 'Credit Score',
            'country': 'Country',
            'gender': 'Gender',
            'age': 'Age',
            'tenure': 'Tenure with Bank',
            'balance': 'Current Bank Balance',
            'products_number': 'No. of Products with Bank',
            'credit_card': 'Credit Card from Bank',
            'active_member': 'Active Member',
            'estimated_salary': 'Estimated Salary'}

INTEGER_FEATURES = ['age', 'tenure', 'products_number']

FLOAT_FEATURES = ['credit_score', 'balance', 'estimated_salary']

CATEGORICAL_FEATURES = ['country', 'gender', 'credit_card', 'active_member']

DEFAULT_FEATURE_VALUES = {
    'credit_score': [692, ""],
    'country': ['France', ['France', 'Germany', 'Spain']],
    'gender' : ['Female', ['Male', 'Female']],
    'age' : [28, ''],
    'tenure' : [8, ''],
    'balance' : [95059, ''],
    'products_number': [2, ''],
    'credit_card' : ['Yes', ['Yes', 'No']],
    'active_member' : ['No', ['Yes', 'No']],
    'estimated_salary' : [44420, '']
}

def get_console_handler():
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    return console_handler


def get_file_handler():
    file_handler = TimedRotatingFileHandler(
        LOG_FILE, when='midnight')
    file_handler.setFormatter(FORMATTER)
    file_handler.setLevel(logging.WARNING)
    return file_handler


def get_logger(*, logger_name):
   
    logger = logging.getLogger(logger_name)

    logger.setLevel(logging.DEBUG)

    logger.addHandler(get_console_handler())
    logger.addHandler(get_file_handler())
    logger.propagate = False

    return logger


class Config:
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    # SECRET_KEY = 'this-really-needs-to-be-changed'
    SERVER_PORT = 5000


class ProductionConfig(Config):
    DEBUG = False
    SERVER_PORT = os.environ.get('PORT', 5000)


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
