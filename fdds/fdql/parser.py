# fdds/fdql/parser.py

class FDQLParser:
    """
    Parses FDQL (Fast Dynamic Query Language) statements into executable commands.
    """

    def __init__(self):
        pass

    def parse(self, query):
        """
        Parses an FDQL query string and returns a structured command.
        
        :param query: A string containing the FDQL query.
        :return: A dictionary or object representing the parsed command.
        """
        query = query.strip().lower()
        
        if query.startswith("create table"):
            return self._parse_create_table(query)
        elif query.startswith("select"):
            return self._parse_select(query)

        raise ValueError(f"Unsupported FDQL command: {query}")

    def _parse_create_table(self, query):
        """
        Parses a CREATE TABLE command.
        
        :param query: The FDQL query string.
        :return: A dictionary representing the CREATE TABLE command.
        """
        tokens = query.split()
        table_name = tokens[2]
        columns_part = query[query.index('(')+1:query.rindex(')')].strip()
        columns = [col.strip().split() for col in columns_part.split(',')]
        columns_dict = {col[0]: eval(col[1]) for col in columns}

        return {
            "command": "create_table",
            "table_name": table_name,
            "columns": columns_dict
        }

    def _parse_select(self, query):
        """
        Parses a SELECT command.
        
        :param query: The FDQL query string.
        :return: A dictionary representing the SELECT command.
        """
        tokens = query.split()
        columns = tokens[1].split(',')
        table_name = tokens[tokens.index('from') + 1]
        
        condition = None
        if "where" in tokens:
            condition = " ".join(tokens[tokens.index('where') + 1:])
        
        return {
            "command": "select",
            "table_name": table_name,
            "columns": columns,
            "condition": condition
        }
