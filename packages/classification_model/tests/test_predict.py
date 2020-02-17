import math

from classification_model.predict import make_prediction
from classification_model.processing.data_helper import load_dataset


def test_make_single_prediction():
    # Given
    test_data = load_dataset(file_name='test.csv')
    single_test_input = test_data[0:1]

    # When
    subject = make_prediction(input_data=single_test_input)

    # Then
    assert subject is not None
    # assert isinstance(subject.get('predictions')[0], int)
    assert math.ceil(subject.get('predictions')[0]) == 5
