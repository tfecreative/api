import bleach
from rest_framework import serializers


class SanitizedCharField(serializers.Field):
    """
    Char field sanitized with bleach
    """

    def clean(self, value):
        return bleach.clean('' if value is None else value)

    def to_representation(self, value):
        return self.clean(value)

    def to_internal_value(self, value):
        return self.clean(value)
