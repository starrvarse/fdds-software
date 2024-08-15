# fdds/storage/mmap_storage.py

import mmap
import os

class MMapStorage:
    """
    Manages memory-mapped file storage for FDDS.
    """

    def __init__(self, storage_path):
        """
        Initializes the memory-mapped storage system.
        
        :param storage_path: The directory where the database files will be stored.
        """
        self.storage_path = storage_path
        if not os.path.exists(storage_path):
            os.makedirs(storage_path)

    def save_table(self, db_name, table_name, table_data):
        """
        Saves a table to a memory-mapped file.
        
        :param db_name: The name of the database.
        :param table_name: The name of the table.
        :param table_data: The data of the table to be saved (must be a byte object).
        """
        file_path = os.path.join(self.storage_path, f"{db_name}_{table_name}.arif")
        with open(file_path, 'wb') as f:
            f.write(table_data)
        
        with open(file_path, 'r+b') as f:
            mm = mmap.mmap(f.fileno(), 0)
            mm[:] = table_data
            mm.flush()
            mm.close()

    def load_table(self, db_name, table_name):
        """
        Loads a table from a memory-mapped file.
        
        :param db_name: The name of the database.
        :param table_name: The name of the table.
        :return: The loaded table data (as bytes).
        """
        file_path = os.path.join(self.storage_path, f"{db_name}_{table_name}.arif")
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Table '{table_name}' not found in database '{db_name}'.")
        
        with open(file_path, 'r+b') as f:
            mm = mmap.mmap(f.fileno(), 0)
            data = mm[:]
            mm.close()
            return data

    def delete_table(self, db_name, table_name):
        """
        Deletes a memory-mapped file.
        
        :param db_name: The name of the database.
        :param table_name: The name of the table.
        """
        file_path = os.path.join(self.storage_path, f"{db_name}_{table_name}.arif")
        if os.path.exists(file_path):
            os.remove(file_path)
        else:
            raise FileNotFoundError(f"Table '{table_name}' not found in database '{db_name}'.")
