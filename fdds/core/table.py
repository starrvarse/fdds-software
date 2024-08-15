# fdds/core/table.py

class Table:
    """
    A class representing a table within a database in FDDS.
    Handles operations such as inserting, deleting, and querying rows.
    """

    def __init__(self, name, columns):
        """
        Initialize a new table.
        
        :param name: The name of the table.
        :param columns: A dictionary defining the column names and their data types.
        """
        self.name = name
        self.columns = columns
        self.rows = []

    def insert(self, row):
        """
        Insert a new row into the table.
        
        :param row: A dictionary representing the row to be inserted.
        """
        if not isinstance(row, dict):
            raise ValueError("Row must be a dictionary.")
        if set(row.keys()) != set(self.columns.keys()):
            raise ValueError("Row keys must match table columns.")
        
        self.rows.append(row)

    def delete(self, condition):
        """
        Delete rows from the table based on a condition.
        
        :param condition: A function that takes a row and returns True if the row should be deleted.
        """
        self.rows = [row for row in self.rows if not condition(row)]

    def query(self, condition=None):
        """
        Query rows in the table.
        
        :param condition: A function that takes a row and returns True if the row should be included.
                          If None, all rows are returned.
        :return: A list of rows that match the condition.
        """
        if condition is None:
            return self.rows
        return [row for row in self.rows if condition(row)]
