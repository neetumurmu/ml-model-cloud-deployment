import numpy as np
from sklearn.model_selection import train_test_split

from classification_model import pipeline
from classification_model.processing.data_helper import (load_dataset, save_pipeline)
from classification_model.config import config
from classification_model import __version__ as _version 

import logging


_logger = logging.getLogger(__name__)


def run_training():

	data = load_dataset(file_name=config.TRAINING_DATA_FILE)

	X_train, X_test, y_train, y_test = train_test_split(
		data[config.FEATURES],
		data[config.TARGET],
		test_size=0.2,
		random_state=6)

	pipeline.clf_pipe.fit(X_train[config.FEATURES], y_train)

	_logger.info(f'saving model version: {_version}')
	save_pipeline(pipeline_to_save=pipeline.clf_pipe)


if __name__ == '__main__':
	run_training()