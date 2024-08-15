# fdds/utils/validation_commands.py

class ValidateRowCommand:
    """
    Command to validate a row against a table's schema in FDDS.
    """

    def __init__(self, validator):
        self.validator = validator

    def execute(self, table_schema, row):
        """
        Executes the command to validate a row against a table's schema.
        
        :param table_schema: The schema of the table (a dictionary of column names and types).
        :param row: The row data to validate (a dictionary).
        :return: A confirmation message or raises an error if validation fails.
        """
        self.validator.validate_row(table_schema, row)
        return f"Row is valid against the table schema."

class ValidateTableNameCommand:
    """
    Command to validate a table name in FDDS.
    """

    def __init__(self, validator):
        self.validator = validator

    def execute(self, table_name):
        """
        Executes the command to validate a table name.
        
        :param table_name: The name of the table to validate.
        :return: A confirmation message or raises an error if validation fails.
        """
        self.validator.validate_table_name(table_name)
        return f"Table name '{table_name}' is valid."

class ValidateColumnNameCommand:
    """
    Command to validate a column name in FDDS.
    """

    def __init__(self, validator):
        self.validator = validator

    def execute(self, column_name):
        """
        Executes the command to validate a column name.
        
        :param column_name: The name of the column to validate.
        :return: A confirmation message or raises an error if validation fails.
        """
        self.validator.validate_column_name(column_name)
        return f"Column name '{column_name}' is valid."
