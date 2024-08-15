# fdds/storage/memory_storage.py

class MemoryStorage:
    """
    Manages in-memory storage for FDDS.
    """

    def __init__(self):
        """
        Initializes the in-memory storage system.
        """
        self.storage = {}

    def save_table(self, db_name, table_name, table_data):
        """
        Saves a table in memory.
        
        :param db_name: The name of the database.
        :param table_name: The name of the table.
        :param table_data: The data of the table to be saved.
        """
        if db_name not in self.storage:
            self.storage[db_name] = {}
        self.storage[db_name][table_name] = table_data

    def load_table(self, db_name, table_name):
        """
        Loads a table from memory.
        
        :param db_name: The name of the database.
        :param table_name: The name of the table.
        :return: The loaded table data.
        """
        if db_name in self.storage and table_name in self.storage[db_name]:
            return self.storage[db_name][table_name]
        else:
            raise KeyError(f"Table '{table_name}' not found in database '{db_name}'.")

    def delete_table(self, db_name, table_name):
        """
        Deletes a table from memory.
        
        :param db_name: The name of the database.
        :param table_name: The name of the table.
        """
        if db_name in self.storage and table_name in self.storage[db_name]:
            del self.storage[db_name][table_name]
        else:
            raise KeyError(f"Table '{table_name}' not found in database '{db_name}'.")
