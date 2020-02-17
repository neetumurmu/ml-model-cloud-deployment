import numpy as numpy
import pandas as pd

from classification_model.processing.data_helper import load_pipeline
from classification_model.config import config
from classification_model import __version__ as _version

import logging
import typing as t


_logger = logging.getLogger(__name__)

pipeline_file_name = f'{config.PIPELINE_SAVE_FILE}{_version}.pkl'
clf_pipe = load_pipeline(file_name=pipeline_file_name)


def make_prediction(*, input_data):
	# input_data should be changed

	data = pd.read_json(input_data)

	prediction = clf_pipe.predict(data[config.FEATURES])

	results = {'predictions': prediction, 'version': _version}

	_logger.info(
		f'Making predictions with model version : {_version}'
		f'Inputs: {data}'
		f'Predictions : {results}')

	return results