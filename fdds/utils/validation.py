# fdds/utils/validation.py

class FDDSValidator:
    """
    Utility for validating data types and schema in FDDS.
    """

    @staticmethod
    def validate_row(table_schema, row):
        """
        Validates that a row conforms to the table schema.
        
        :param table_schema: Dictionary defining the column names and their expected data types.
        :param row: Dictionary representing the row to be validated.
        :return: True if valid, raises ValueError if invalid.
        """
        for column, expected_type in table_schema.items():
            if column not in row:
                raise ValueError(f"Missing column '{column}' in row.")
            if not isinstance(row[column], expected_type):
                raise ValueError(f"Invalid type for column '{column}': expected {expected_type}, got {type(row[column])}.")
        return True

    @staticmethod
    def validate_table_name(table_name):
        """
        Validates the table name to ensure it meets naming conventions.
        
        :param table_name: The name of the table.
        :return: True if valid, raises ValueError if invalid.
        """
        if not isinstance(table_name, str) or not table_name.isidentifier():
            raise ValueError(f"Invalid table name '{table_name}'. It must be a valid identifier.")
        return True

    @staticmethod
    def validate_column_name(column_name):
        """
        Validates the column name to ensure it meets naming conventions.
        
        :param column_name: The name of the column.
        :return: True if valid, raises ValueError if invalid.
        """
        if not isinstance(column_name, str) or not column_name.isidentifier():
            raise ValueError(f"Invalid column name '{column_name}'. It must be a valid identifier.")
        return True
