import re

from django.core.exceptions import ValidationError


def hex_validator(value):
    if not re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', value):
        raise ValidationError(f'{value} не соответствует формату HEX.')
