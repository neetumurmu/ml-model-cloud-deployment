from marshmallow import Schema, fields
from marshmallow import ValidationError

import typing as t
import json


class InvalidInputError(Exception):
    """Invalid model input."""


SYNTAX_ERROR_FIELD_MAP = {
    '1stFlrSF': 'FirstFlrSF',
    '2ndFlrSF': 'SecondFlrSF',
    '3SsnPorch': 'ThreeSsnPortch'
}


class HouseDataRequestSchema(Schema):
    Elevation = fields.Integer()
    Aspect = fields.Integer()
    Slope = fields.Integer()
    Horizontal_Distance_To_Hydrology = fields.Integer()
    Vertical_Distance_To_Hydrology = fields.Integer()
    Horizontal_Distance_To_Roadways = fields.Integer()
    Hillshade_9am = fields.Integer()
    Hillshade_Noon = fields.Integer()
    Hillshade_3pm = fields.Integer()
    Horizontal_Distance_To_Fire_Points = fields.Integer()
    Wilderness_Area1 = fields.Integer()
    Wilderness_Area2 = fields.Integer()
    Wilderness_Area3 = fields.Integer()
    Wilderness_Area4 = fields.Integer()
    Soil_Type1 = fields.Integer()
    Soil_Type2 = fields.Integer()
    Soil_Type3 = fields.Integer()
    Soil_Type4 = fields.Integer()
    Soil_Type5 = fields.Integer()
    Soil_Type6 = fields.Integer()
    Soil_Type7 = fields.Integer()
    Soil_Type8 = fields.Integer()
    Soil_Type9 = fields.Integer()
    Soil_Type10 = fields.Integer()
    Soil_Type11 = fields.Integer()
    Soil_Type12 = fields.Integer()
    Soil_Type13 = fields.Integer()
    Soil_Type14 = fields.Integer()
    Soil_Type15 = fields.Integer()
    Soil_Type16 = fields.Integer()
    Soil_Type17 = fields.Integer()
    Soil_Type18 = fields.Integer()
    Soil_Type19 = fields.Integer()
    Soil_Type20 = fields.Integer()
    Soil_Type21 = fields.Integer()
    Soil_Type22 = fields.Integer()
    Soil_Type23 = fields.Integer()
    Soil_Type24 = fields.Integer()
    Soil_Type25 = fields.Integer()
    Soil_Type26 = fields.Integer()
    Soil_Type27 = fields.Integer()
    Soil_Type28 = fields.Integer()
    Soil_Type29 = fields.Integer()
    Soil_Type30 = fields.Integer()
    Soil_Type31 = fields.Integer()
    Soil_Type32 = fields.Integer()
    Soil_Type33 = fields.Integer()
    Soil_Type34 = fields.Integer()
    Soil_Type35 = fields.Integer()
    Soil_Type36 = fields.Integer()
    Soil_Type37 = fields.Integer()
    Soil_Type38 = fields.Integer()
    Soil_Type39 = fields.Integer()
    Soil_Type40 = fields.Integer()


def _filter_error_rows(errors: dict,
                       validated_input: t.List[dict]
                       ) -> t.List[dict]:
    """Remove input data rows with errors."""

    indexes = errors.keys()
    # delete them in reverse order so that you
    # don't throw off the subsequent indexes.
    for index in sorted(indexes, reverse=True):
        del validated_input[index]

    return validated_input


def validate_inputs(input_data):
    """Check prediction inputs against schema."""

    # set many=True to allow passing in a list
    schema = HouseDataRequestSchema(strict=True, many=True)

    # convert syntax error field names (beginning with numbers)
    for dict in input_data:
        for key, value in SYNTAX_ERROR_FIELD_MAP.items():
            dict[value] = dict[key]
            del dict[key]

    errors = None
    try:
        schema.load(input_data)
    except ValidationError as exc:
        errors = exc.messages

    # convert syntax error field names back
    # this is a hack - never name your data
    # fields with numbers as the first letter.
    for dict in input_data:
        for key, value in SYNTAX_ERROR_FIELD_MAP.items():
            dict[key] = dict[value]
            del dict[value]

    if errors:
        validated_input = _filter_error_rows(
            errors=errors,
            validated_input=input_data)
    else:
        validated_input = input_data

    return validated_input, errors
