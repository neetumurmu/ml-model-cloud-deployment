from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler

from classification_model.processing import preprocessors as pp 
from classification_model.processing import features
from classification_model.config import config

import logging

_logger = logging.getLogger(__name__)


clf_pipe = Pipeline(
	[
		# ('hydrology_features',
		# 	features.HydrologyFeatures()),
		# ('kernel_features',
		# 	features.KernelFeatures()),
		# ('scaler', MinMaxScaler()),
		('rf_model', RandomForestClassifier(n_estimators=100, random_state=6))
	]

)


# clf_pipe = Pipeline(
# 	[
# 		('aspect_binning',
# 			features.AspectBinning()),
# 		('hydrology_features',
# 			features.HydrologyFeatures()),
# 		('kernel_features',
# 			features.KernelFeatures()),
# 		('scaler', MinMaxScaler()),
# 		('rf_model', RandomForestClassifier(random_state=6))
# 	]
# )