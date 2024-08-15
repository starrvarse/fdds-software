# fdds/models/fields.py

class Field:
    """
    Base class for all field types in FDDS.
    """

    def __init__(self, required=False, default=None):
        self.required = required
        self.default = default

    def validate(self, value):
        """
        Validates the field value.
        
        :param value: The value to validate.
        :return: True if valid, raises ValueError if invalid.
        """
        if self.required and value is None:
            raise ValueError("This field is required.")
        return True

class IntegerField(Field):
    """
    Field type for integers.
    """

    def validate(self, value):
        super().validate(value)
        if not isinstance(value, int):
            raise ValueError(f"Expected an integer, got {type(value).__name__}.")
        return True

class StringField(Field):
    """
    Field type for strings.
    """

    def validate(self, value):
        super().validate(value)
        if not isinstance(value, str):
            raise ValueError(f"Expected a string, got {type(value).__name__}.")
        return True

class BooleanField(Field):
    """
    Field type for booleans.
    """

    def validate(self, value):
        super().validate(value)
        if not isinstance(value, bool):
            raise ValueError(f"Expected a boolean, got {type(value).__name__}.")
        return True
