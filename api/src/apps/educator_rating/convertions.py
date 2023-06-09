from typing import Optional

from .models import (EducatorIndicatorValue,
                     EducatorRatingPartition,
                     EducatorReport)
from ..rating.models import Criterion
from ..rating.models import ValueType


DataTypes = ValueType.DataTypes


def get_formatted_criterion_key(
    partition_abbr: str,
    number: int,
    subnumber: Optional[int]
) -> str:
    number = str(number).zfill(2)

    if subnumber is None:
        return f'{partition_abbr}{number}'
    else:
        return f'{partition_abbr}{number}_{subnumber}'


def convert_to_float(multitype_value: dict) -> float:
    match multitype_value:
        case {'value': bool() as value, 'type': DataTypes.BOOL.value}:
            return float(value)
        case {'value': int() as value, 'type': DataTypes.INT.value}:
            return float(value)
        case {'value': float() as value, 'type': DataTypes.FLOAT.value}:
            return value
        case {'value': str(), 'type': DataTypes.STR.value}:
            return 0.0
        case _:
            return 0.0


def bundle_report(report: EducatorReport) -> dict:
    ''' Create dictionary object with all neccessary information
    about given report.

    The structure of the dictionary is as follows:
    {
        'year': <int>,
        'educatorPersonalNumber': <str>,
        'values': [
            {
                'criterionKey': <str>,      # Examples: "П01" / "А15" / "О03_1"
                'criterionValue': <float>
            },
            ...
            {...}
        ]
    }
    '''

    data = dict()

    data['year'] = report.year
    data['educatorPersonalNumber'] = report.educator.personal_number
    data['values'] = []

    educator_partitions = EducatorRatingPartition.objects.all(
    ).values_list('partition')

    report_criterions = Criterion.objects.filter(
        partition__in=educator_partitions
    ).order_by(
        'partition', 'number', 'subnumber'
    ).select_related('partition', 'indicator')

    indicator_values = EducatorIndicatorValue.objects.filter(
        report=report
    ).select_related('indicator')

    for criterion in report_criterions:
        indicator_value = indicator_values.get(
            indicator=criterion.indicator
        ).value

        data['values'].append(
            {
                'criterionKey': get_formatted_criterion_key(
                    criterion.partition.abbreviation,
                    criterion.number,
                    criterion.subnumber
                ),
                'criterionValue': convert_to_float(indicator_value)
            }
        )

    return data
