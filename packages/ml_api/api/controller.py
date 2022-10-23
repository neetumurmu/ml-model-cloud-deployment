from flask import Blueprint, request, jsonify,  render_template, request, redirect
from classification_model.predict import make_prediction
from classification_model import __version__ as _version 
from api.config import (FEATURES, DEFAULT_FEATURE_VALUES, INTEGER_FEATURES,
                        FLOAT_FEATURES, CATEGORICAL_FEATURES)
import os
from werkzeug.utils import secure_filename
from api.config import get_logger
# from api.validation import validate_inputs, allowed_file
from api import __version__ as api_version



_logger = get_logger(logger_name=__name__)


prediction_app = Blueprint('prediction_app', __name__)

@prediction_app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        form_content = {}
        for feat in FEATURES:
            if feat in ['credit_card', 'active_member']:
                form_content[feat] = 1 if request.form[feat] == 'Yes' else 0
            elif feat in INTEGER_FEATURES:
                form_content[feat] = int(request.form[feat])
            elif feat in FLOAT_FEATURES:
                form_content[feat] = float(request.form[feat])
            else:
                form_content[feat] = request.form[feat]


        output = predict(form_content, index_data=True)
        print(output)
        output = 'Yes' if output['predictions'][0] else 'No'

        return render_template('index.html',
                                 prediction_data=[form_content, output],
                                 feature_fields=FEATURES,
                                 default_feature_values=DEFAULT_FEATURE_VALUES,
                                 integer_features=INTEGER_FEATURES,
                                 float_features=FLOAT_FEATURES,
                                 categorical_features=CATEGORICAL_FEATURES)
    else:
        return render_template('index.html',
                                 feature_fields=FEATURES,
                                 default_feature_values=DEFAULT_FEATURE_VALUES,
                                 integer_features=INTEGER_FEATURES,
                                 float_features=FLOAT_FEATURES,
                                 categorical_features=CATEGORICAL_FEATURES
                                 )

@prediction_app.route('/health', methods=['GET'])
def health():
	if request.method == 'GET':
		_logger.info('health status OK')
		return 'ok'

@prediction_app.route('/version', methods=['GET'])
def version():
    if request.method == 'GET':
        return jsonify({'model_version': _version,
                        'api_version': api_version})

# @prediction_app.route('/v1/predict/classification', methods=['POST'])
def predict(input_data, index_data=False):
    # Step 1: Extract POST data from request body as JSON
    _logger.debug(f'Inputs: {input_data}')

    # Step 2: Validate the input using marshmallow schema
    # input_data, errors = validate_inputs(input_data=json_data)

    # Step 3: Model prediction
    result = make_prediction(input_data=input_data, index_data=index_data)
    _logger.debug(f'Outputs: {result}')

    # Step 4: Convert numpy ndarray to list
    predictions = result.get('predictions').tolist()
    version = result.get('version')

        # Step 5: Return the response as JSON
    return {'predictions': predictions,
                        'version': version}