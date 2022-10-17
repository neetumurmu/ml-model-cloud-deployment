import math

from classification_model.predict import make_prediction
from classification_model.processing.data_helper import load_dataset
from classification_model.config import config


def test_make_single_prediction():
    # Given
    test_data = load_dataset(file_name='test.csv')
    start, end = 3, 4
    single_test_input = test_data[start:end][config.FEATURES]
    output = test_data[start:end][config.TARGET]

    # When
    subject = make_prediction(input_data=single_test_input)
    
    # Then
    assert subject is not None
    # assert isinstance(subject.get('predictions')[0], int)
    assert math.ceil(subject.get('predictions')[0]) == 1
