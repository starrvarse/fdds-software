# fdds/fdql/query_builder.py

class FDQLQueryBuilder:
    """
    Builds FDQL queries programmatically.
    """

    def __init__(self):
        self._select = []
        self._from = None
        self._where = None
        self._order_by = None
        self._group_by = None

    def select(self, *columns):
        """
        Specifies the columns to select in the query.
        
        :param columns: Column names to select.
        :return: Self, for chaining.
        """
        self._select = columns
        return self

    def from_table(self, table_name):
        """
        Specifies the table to select from.
        
        :param table_name: The name of the table.
        :return: Self, for chaining.
        """
        self._from = table_name
        return self

    def where(self, condition):
        """
        Specifies the condition for the WHERE clause.
        
        :param condition: The condition to filter rows.
        :return: Self, for chaining.
        """
        self._where = condition
        return self

    def order_by(self, *columns):
        """
        Specifies the columns to order by.
        
        :param columns: Column names to order by.
        :return: Self, for chaining.
        """
        self._order_by = columns
        return self

    def group_by(self, *columns):
        """
        Specifies the columns to group by.
        
        :param columns: Column names to group by.
        :return: Self, for chaining.
        """
        self._group_by = columns
        return self

    def build(self):
        """
        Builds and returns the FDQL query string.
        
        :return: The FDQL query string.
        """
        query = "SELECT " + ", ".join(self._select)
        query += " FROM " + self._from
        if self._where:
            query += " WHERE " + self._where
        if self._group_by:
            query += " GROUP BY " + ", ".join(self._group_by)
        if self._order_by:
            query += " ORDER BY " + ", ".join(self._order_by)
        return query
