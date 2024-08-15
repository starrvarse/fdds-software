# fdds/fdql/fdql_commands.py

from fdds.fdql.parser import FDQLParser
from fdds.fdql.commands import FDQLExecutor

class ExecuteFDQLCommand:
    """
    Command to execute an FDQL query in FDDS.
    """

    def __init__(self, engine):
        self.parser = FDQLParser()
        self.executor = FDQLExecutor(engine)

    def execute(self, query):
        """
        Executes the FDQL query.
        
        :param query: The FDQL query string to execute.
        :return: The result of the query execution.
        """
        parsed_query = self.parser.parse(query)
        result = self.executor.execute(parsed_query)
        return result

class ExplainFDQLCommand:
    """
    Command to explain an FDQL query without executing it.
    """

    def __init__(self, engine):
        self.parser = FDQLParser()

    def execute(self, query):
        """
        Explains the FDQL query.
        
        :param query: The FDQL query string to explain.
        :return: A string explaining the query.
        """
        parsed_query = self.parser.parse(query)
        return f"FDQL Query Explanation: {parsed_query}"
