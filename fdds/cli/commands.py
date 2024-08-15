# fdds/cli/commands.py

class Command:
    """
    Base class for all commands in FDDS.
    """

    def execute(self, *args, **kwargs):
        """
        Executes the command with given arguments.
        """
        raise NotImplementedError("Subclasses must implement the execute method.")

class CreateDatabaseCommand(Command):
    """
    Command to create a new database in FDDS.
    """

    def __init__(self, engine):
        self.engine = engine

    def execute(self, db_name):
        """
        Executes the command to create a new database.
        
        :param db_name: The name of the database to create.
        """
        self.engine.create_database(db_name)
        return f"Database '{db_name}' created successfully."

class DropDatabaseCommand(Command):
    """
    Command to drop an existing database in FDDS.
    """

    def __init__(self, engine):
        self.engine = engine

    def execute(self, db_name):
        """
        Executes the command to drop an existing database.
        
        :param db_name: The name of the database to drop.
        """
        self.engine.delete_database(db_name)
        return f"Database '{db_name}' deleted successfully."

class ListDatabasesCommand(Command):
    """
    Command to list all databases in FDDS.
    """

    def __init__(self, engine):
        self.engine = engine

    def execute(self):
        """
        Executes the command to list all databases.
        
        :return: A list of database names.
        """
        return self.engine.list_databases()
