import os
import pickle
from .table import Table

class FDDSEngine:
    """
    The core database engine for the Fast Dynamic Database System (FDDS).
    Handles data storage, retrieval, and basic operations.
    """

    def __init__(self, storage_path="fdds_data"):
        self.storage_path = storage_path
        self.databases = {}
        self.load_databases()

    def create_database(self, name):
        """
        Creates a new database.
        
        :param name: The name of the database to create.
        """
        if name in self.databases:
            raise ValueError(f"Database '{name}' already exists.")
        self.databases[name] = {}
        self.save_database(name)

    def delete_database(self, name):
        """
        Deletes an existing database.
        
        :param name: The name of the database to delete.
        """
        if name not in self.databases:
            raise ValueError(f"Database '{name}' does not exist.")
        del self.databases[name]
        os.remove(os.path.join(self.storage_path, f"{name}.pkl"))

    def list_databases(self):
        """
        Lists all the databases.
        
        :return: A list of database names.
        """
        return list(self.databases.keys())

    def get_database(self, name):
        """
        Retrieves a database by name.
        
        :param name: The name of the database to retrieve.
        :return: The database object.
        """
        if name not in self.databases:
            raise ValueError(f"Database '{name}' does not exist.")
        return self.databases[name]

    def create_table(self, db_name, table_name, columns):
        """
        Creates a new table in a specified database.
        
        :param db_name: The name of the database where the table should be created.
        :param table_name: The name of the table to create.
        :param columns: A dictionary defining the column names and their data types.
        """
        database = self.get_database(db_name)
        if table_name in database:
            raise ValueError(f"Table '{table_name}' already exists in database '{db_name}'.")
        database[table_name] = Table(table_name, columns)
        self.save_database(db_name)

    def delete_table(self, db_name, table_name):
        """
        Deletes a table from a specified database.
        
        :param db_name: The name of the database where the table should be deleted.
        :param table_name: The name of the table to delete.
        """
        database = self.get_database(db_name)
        if table_name not in database:
            raise ValueError(f"Table '{table_name}' does not exist in database '{db_name}'.")
        del database[table_name]
        self.save_database(db_name)

    def list_tables(self, db_name):
        """
        Lists all tables in a specified database.
        
        :param db_name: The name of the database to list tables from.
        :return: A list of table names.
        """
        database = self.get_database(db_name)
        return list(database.keys())

    def get_table(self, db_name, table_name):
        """
        Retrieves a table by name from a specified database.
        
        :param db_name: The name of the database where the table resides.
        :param table_name: The name of the table to retrieve.
        :return: The table object.
        """
        database = self.get_database(db_name)
        if table_name not in database:
            raise ValueError(f"Table '{table_name}' does not exist in database '{db_name}'.")
        return database[table_name]

    def save_database(self, name):
        """
        Saves the specified database to disk.
        
        :param name: The name of the database to save.
        """
        os.makedirs(self.storage_path, exist_ok=True)
        db_path = os.path.join(self.storage_path, f"{name}.pkl")
        with open(db_path, "wb") as db_file:
            pickle.dump(self.databases[name], db_file)

    def load_databases(self):
        """
        Loads all databases from disk.
        """
        if not os.path.exists(self.storage_path):
            return

        for filename in os.listdir(self.storage_path):
            if filename.endswith(".pkl"):
                db_name = filename[:-4]
                with open(os.path.join(self.storage_path, filename), "rb") as db_file:
                    self.databases[db_name] = pickle.load(db_file)

    def execute_fdql(self, query):
        """
        Executes an FDQL query on the database.
        
        :param query: The FDQL query to execute.
        :return: The result of the query.
        """
        query = query.lower()

        if query.startswith("create database"):
            db_name = query.split()[-1]
            self.create_database(db_name)
            return f"Database '{db_name}' created successfully."

        elif query.startswith("create table"):
            parts = query.split("(")
            table_info = parts[0].split()
            db_table = table_info[2].split(".")
            db_name = db_table[0]
            table_name = db_table[1]
            columns_part = parts[1].strip(")")
            columns = {}
            for col in columns_part.split(","):
                col_name, col_type = col.strip().split()
                if col_type == 'int':
                    col_type = int
                elif col_type == 'str':
                    col_type = str
                else:
                    return f"Unsupported column type '{col_type}'."
                columns[col_name] = col_type
            self.create_table(db_name, table_name, columns)
            return f"Table '{table_name}' created successfully in database '{db_name}'."

        elif query.startswith("insert into"):
            parts = query.split("values")
            table_info = parts[0].split()[2]
            db_table = table_info.split(".")
            db_name = db_table[0]
            table_name = db_table[1]
            values_part = parts[1].strip("() ")
            values = [eval(val.strip()) for val in values_part.split(",")]
            table = self.get_table(db_name, table_name)
            columns = list(table.columns.keys())
            row_data = dict(zip(columns, values))
            table.insert(row_data)
            self.save_database(db_name)
            return f"Record inserted successfully into '{table_name}' in database '{db_name}'."

        elif query.startswith("select * from"):
            table_info = query.split()[3].split(".")
            db_name = table_info[0]
            table_name = table_info[1]
            table = self.get_table(db_name, table_name)
            results = table.query()  # Assuming `query()` returns all rows
            return {"status": "success", "result": results}

        elif query.startswith("delete from"):
            parts = query.split("where")
            table_info = parts[0].split()[2].split(".")
            condition = parts[1].strip().split("=")
            db_name = table_info[0]
            table_name = table_info[1]
            column = condition[0].strip()
            value = eval(condition[1].strip())
            table = self.get_table(db_name, table_name)
            table.delete(lambda row: row[column] == value)
            self.save_database(db_name)
            return f"Record deleted successfully from '{table_name}' in database '{db_name}'."

        elif query.startswith("drop table"):
            db_table = query.split()[2].split(".")
            db_name = db_table[0]
            table_name = db_table[1]
            self.delete_table(db_name, table_name)
            return f"Table '{table_name}' deleted successfully from database '{db_name}'."

        elif query.startswith("drop database"):
            db_name = query.split()[-1]
            self.delete_database(db_name)
            return f"Database '{db_name}' deleted successfully."

        else:
            return "Unsupported FDQL query."

# Example usage
if __name__ == "__main__":
    engine = FDDSEngine()
    engine.create_database("test_db")
    engine.create_table("test_db", "users", {"id": int, "name": str, "email": str})
    
    users_table = engine.get_table("test_db", "users")
    users_table.insert({"id": 1, "name": "Alice", "email": "alice@example.com"})
    users_table.insert({"id": 2, "name": "Bob", "email": "bob@example.com"})
    
    print("All users:", users_table.query())
    users_table.delete(lambda row: row["id"] == 1)
    print("Users after deletion:", users_table.query())

    print("Databases:", engine.list_databases())
    print("Tables in 'test_db':", engine.list_tables("test_db"))
    
    engine.delete_table("test_db", "users")
    engine.delete_database("test_db")
    print("Databases after deletion:", engine.list_databases())
