# fdds/models/views.py

class View:
    """
    Represents a virtual table (view) in FDDS.
    """

    def __init__(self, name, query, engine):
        """
        Initializes the view.
        
        :param name: The name of the view.
        :param query: The query that defines the view.
        :param engine: The FDDSEngine instance to execute the query.
        """
        self.name = name
        self.query = query
        self.engine = engine

    def execute(self):
        """
        Executes the view's query and returns the result.
        
        :return: The result of the query.
        """
        parser = self.engine.parser
        executor = self.engine.executor
        parsed_query = parser.parse(self.query)
        return executor.execute(parsed_query)

class ViewManager:
    """
    Manages views in FDDS.
    """

    def __init__(self):
        self.views = {}

    def create_view(self, name, query, engine):
        """
        Creates a new view.
        
        :param name: The name of the view.
        :param query: The query that defines the view.
        :param engine: The FDDSEngine instance to execute the query.
        """
        if name in self.views:
            raise ValueError(f"View '{name}' already exists.")
        self.views[name] = View(name, query, engine)

    def drop_view(self, name):
        """
        Drops an existing view.
        
        :param name: The name of the view to drop.
        """
        if name not in self.views:
            raise ValueError(f"View '{name}' does not exist.")
        del self.views[name]

    def execute_view(self, name):
        """
        Executes a view and returns the result.
        
        :param name: The name of the view to execute.
        :return: The result of the view's query.
        """
        if name not in self.views:
            raise ValueError(f"View '{name}' does not exist.")
        return self.views[name].execute()
