# fdds/fdql/stored_procedure.py

class StoredProcedure:
    def __init__(self, name, procedure_body):
        self.name = name
        self.procedure_body = procedure_body

    def execute(self, *args, **kwargs):
        """
        Executes the stored procedure.
        
        :param args: Positional arguments for the procedure.
        :param kwargs: Keyword arguments for the procedure.
        :return: The result of the procedure execution.
        """
        return self.procedure_body(*args, **kwargs)

class StoredProcedureManager:
    def __init__(self):
        self.procedures = {}

    def create_procedure(self, name, procedure_body):
        """
        Creates a new stored procedure.
        
        :param name: The name of the procedure.
        :param procedure_body: The body of the procedure (a function).
        """
        self.procedures[name] = StoredProcedure(name, procedure_body)

    def execute_procedure(self, name, *args, **kwargs):
        """
        Executes a stored procedure.
        
        :param name: The name of the procedure.
        :param args: Positional arguments.
        :param kwargs: Keyword arguments.
        :return: The result of the procedure execution.
        """
        if name in self.procedures:
            return self.procedures[name].execute(*args, **kwargs)
        else:
            raise ValueError(f"Stored procedure '{name}' not found.")
