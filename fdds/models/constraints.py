# fdds/models/constraints.py

class Constraint:
    """
    Base class for all constraints in FDDS.
    """

    def __init__(self, name):
        self.name = name

    def validate(self, table, row):
        """
        Validates the constraint.
        
        :param table: The table object where the constraint is applied.
        :param row: The row of data to validate.
        :return: True if valid, raises ValueError if invalid.
        """
        raise NotImplementedError("Subclasses must implement this method.")

class PrimaryKeyConstraint(Constraint):
    """
    Enforces a primary key constraint on a column.
    """

    def validate(self, table, row):
        key = row.get(self.name)
        for existing_row in table.query():
            if existing_row.get(self.name) == key:
                raise ValueError(f"Primary key constraint violated: {self.name} must be unique.")
        return True

class UniqueConstraint(Constraint):
    """
    Enforces a unique constraint on a column.
    """

    def validate(self, table, row):
        value = row.get(self.name)
        for existing_row in table.query():
            if existing_row.get(self.name) == value:
                raise ValueError(f"Unique constraint violated: {self.name} must be unique.")
        return True

class ForeignKeyConstraint(Constraint):
    """
    Enforces a foreign key constraint between two tables.
    """

    def __init__(self, name, reference_table, reference_column):
        super().__init__(name)
        self.reference_table = reference_table
        self.reference_column = reference_column

    def validate(self, table, row):
        value = row.get(self.name)
        found = False
        for ref_row in self.reference_table.query():
            if ref_row.get(self.reference_column) == value:
                found = True
                break
        if not found:
            raise ValueError(f"Foreign key constraint violated: {self.name} must reference an existing value in {self.reference_table.name}.{self.reference_column}.")
        return True
