from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from .models import ValueType

DataTypes = ValueType.DataTypes


class IndicatorValueValidationError(ValidationError):
    pass


def validate_indicator_value(value: dict) -> None:
    match value:
        case {'value': bool(), 'type': DataTypes.BOOL.value}:
            pass
        case {'value': int(), 'type': DataTypes.INT.value}:
            pass
        case {'value': float() | int(), 'type': DataTypes.FLOAT.value}:
            pass
        case {'value': str(), 'type': DataTypes.STR.value}:
            pass
        case _:
            raise IndicatorValueValidationError(_("Wrong JSON format."))
