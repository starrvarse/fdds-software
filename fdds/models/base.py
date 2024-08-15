# fdds/models/base.py

class BaseModel:
    """
    Base class for data models in FDDS.
    Provides basic methods for interacting with table data.
    """

    def __init__(self, table, **kwargs):
        """
        Initializes a data model instance.
        
        :param table: The table associated with this model.
        :param kwargs: Key-value pairs representing the initial data.
        """
        self._table = table
        self._data = kwargs

    def save(self):
        """
        Saves the current instance to the table.
        """
        self._table.insert(self._data)

    def delete(self):
        """
        Deletes the current instance from the table.
        """
        self._table.delete(lambda row: all(row[k] == v for k, v in self._data.items()))

    @classmethod
    def all(cls, table):
        """
        Retrieves all instances from the table.
        
        :param table: The table from which to retrieve data.
        :return: A list of model instances.
        """
        rows = table.query()
        return [cls(table, **row) for row in rows]

    @classmethod
    def filter(cls, table, **conditions):
        """
        Filters instances from the table based on conditions.
        
        :param table: The table from which to retrieve data.
        :param conditions: Key-value pairs representing filter conditions.
        :return: A list of model instances that match the conditions.
        """
        def condition_func(row):
            return all(row.get(k) == v for k, v in conditions.items())
        
        rows = table.query(condition_func)
        return [cls(table, **row) for row in rows]
