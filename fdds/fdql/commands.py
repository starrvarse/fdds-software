# fdds/fdql/commands.py

class FDQLExecutor:
    """
    Executes parsed FDQL commands using the FDDSEngine.
    """

    def __init__(self, engine):
        """
        Initializes the FDQLExecutor with a reference to the FDDSEngine.
        
        :param engine: An instance of FDDSEngine.
        """
        self.engine = engine

    def execute(self, command):
        """
        Executes a parsed FDQL command.
        
        :param command: The parsed command dictionary from FDQLParser.
        :return: The result of the command execution.
        """
        if command['command'] == 'create_table':
            return self._execute_create_table(command)
        elif command['command'] == 'select':
            return self._execute_select(command)

        raise ValueError(f"Unsupported FDQL command: {command['command']}")

    def _execute_create_table(self, command):
        """
        Executes a CREATE TABLE command.
        
        :param command: The parsed CREATE TABLE command dictionary.
        """
        db_name = "default"  # Default database, replace with actual logic if needed
        self.engine.create_table(db_name, command['table_name'], command['columns'])
        return f"Table '{command['table_name']}' created successfully."

    def _execute_select(self, command):
        """
        Executes a SELECT command.
        
        :param command: The parsed SELECT command dictionary.
        :return: The result of the query.
        """
        table = self.engine.get_table("default", command['table_name'])  # Default database
        if command['condition']:
            condition_func = lambda row: eval(command['condition'])  # Unsafe, replace with safer logic
            return table.query(condition_func)
        return table.query()
