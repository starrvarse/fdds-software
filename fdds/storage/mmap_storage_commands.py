# fdds/storage/mmap_storage_commands.py

class SaveTableMMapCommand:
    """
    Command to save a table using memory-mapped storage in FDDS.
    """

    def __init__(self, mmap_storage):
        self.mmap_storage = mmap_storage

    def execute(self, db_name, table_name, table_data):
        """
        Executes the command to save a table using memory-mapped storage.
        
        :param db_name: The name of the database.
        :param table_name: The name of the table.
        :param table_data: The data of the table to be saved.
        :return: A confirmation message.
        """
        self.mmap_storage.save_table(db_name, table_name, table_data)
        return f"Table '{table_name}' in database '{db_name}' saved successfully using memory-mapped storage."

class LoadTableMMapCommand:
    """
    Command to load a table using memory-mapped storage in FDDS.
    """

    def __init__(self, mmap_storage):
        self.mmap_storage = mmap_storage

    def execute(self, db_name, table_name):
        """
        Executes the command to load a table using memory-mapped storage.
        
        :param db_name: The name of the database.
        :param table_name: The name of the table to load.
        :return: The loaded table data.
        """
        table_data = self.mmap_storage.load_table(db_name, table_name)
        return table_data

class DeleteTableMMapCommand:
    """
    Command to delete a table using memory-mapped storage in FDDS.
    """

    def __init__(self, mmap_storage):
        self.mmap_storage = mmap_storage

    def execute(self, db_name, table_name):
        """
        Executes the command to delete a table using memory-mapped storage.
        
        :param db_name: The name of the database.
        :param table_name: The name of the table to delete.
        :return: A confirmation message.
        """
        self.mmap_storage.delete_table(db_name, table_name)
        return f"Table '{table_name}' in database '{db_name}' deleted successfully using memory-mapped storage."
