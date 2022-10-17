from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, LabelEncoder

from classification_model.processing import preprocessors as pp 
from classification_model.processing import features
from classification_model.config import config

import logging

_logger = logging.getLogger(__name__)


preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), config.FEATURES)
    ]
)

clf_pipe = Pipeline(
	[
		(
            "categorical_encoder",
            pp.CategoricalEncoder(variables=config.CATEGORICAL_VARS),
        ),
		("preprocessor", preprocessor),
		("rf_model", RandomForestClassifier(n_estimators=100, random_state=6))
	]

)
