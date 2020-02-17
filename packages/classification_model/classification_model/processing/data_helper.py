import pandas as pd
import joblib
from sklearn.pipeline import Pipeline 

from classification_model.config import config
from classification_model import __version__ as _version # check this later

import logging 
import typing as t 


_logger = logging.getLogger(__name__)


def load_dataset(*, file_name: str
                 ) -> pd.DataFrame:
    _data = pd.read_csv(f'{config.DATASET_DIR}/{file_name}')
    return _data


def save_pipeline(pipeline_to_save):
	save_file_name = f'{config.PIPELINE_SAVE_FILE}{_version}.pkl'
	save_path = config.TRAINED_MODEL_DIR / save_file_name

	# remove old pipeline if there is any
	remove_old_pipelines(files_to_keep=save_file_name)
	joblib.dump(pipeline_to_save, save_path)
	_logger.info(f'saved pipeline : {save_file_name}')


def load_pipeline(file_name):
	file_path = config.TRAINED_MODEL_DIR / file_name
	trained_model = joblib.load(filename=file_path)
	return trained_model


def remove_old_pipelines(files_to_keep):
	do_not_delete = [files_to_keep + '__init__.py']
	for model_file in config.TRAINED_MODEL_DIR.iterdir():
		if model_file.name not in do_not_delete:
			model_file.unlink()