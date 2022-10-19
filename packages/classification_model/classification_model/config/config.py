import os
import pathlib
import classification_model
import pandas as pd


PACKAGE_ROOT = pathlib.Path(classification_model.__file__).resolve().parent
TRAINED_MODEL_DIR = PACKAGE_ROOT / 'trained_models'
DATASET_DIR = PACKAGE_ROOT / 'datasets'

TESTING_DATA_FILE = 'test.csv'
TRAINING_DATA_FILE = 'Bank Customer Churn Prediction.csv'
TARGET = 'churn'

FEATURES = ['credit_score', 'country', 'gender', 'age', 'tenure', 'balance',
              'products_number', 'credit_card', 'active_member', 'estimated_salary']


CATEGORICAL_VARS = ['country', 'gender']
DROP_FEATURES = []

PIPELINE_NAME = 'random_forest'
PIPELINE_SAVE_FILE = f'{PIPELINE_NAME}_output_v'
