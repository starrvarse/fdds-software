from fdds.indexing.btree import BTree
from fdds.indexing.hashindex import HashIndex
from fdds.indexing.fulltext import FullTextIndex

class CreateBTreeIndexCommand:
    """
    Command to create a B-tree index on a table in FDDS.
    """

    def __init__(self, engine):
        self.engine = engine

    def execute(self, db_name, table_name, column_name):
        """
        Executes the command to create a B-tree index.
        
        :param db_name: The name of the database.
        :param table_name: The name of the table.
        :param column_name: The column to index.
        :return: A confirmation message.
        """
        table = self.engine.get_table(db_name, table_name)
        index = BTree(t=2)  # Example degree, can be parameterized
        for row in table.query():
            index.insert(row[column_name])
        table.indexes[column_name] = index
        return f"B-tree index on '{column_name}' in table '{table_name}' created successfully."

class CreateHashIndexCommand:
    """
    Command to create a hash index on a table in FDDS.
    """

    def __init__(self, engine):
        self.engine = engine

    def execute(self, db_name, table_name, column_name):
        """
        Executes the command to create a hash index.
        
        :param db_name: The name of the database.
        :param table_name: The name of the table.
        :param column_name: The column to index.
        :return: A confirmation message.
        """
        table = self.engine.get_table(db_name, table_name)
        index = HashIndex()
        for row in table.query():
            index.insert(row[column_name], row)
        table.indexes[column_name] = index
        return f"Hash index on '{column_name}' in table '{table_name}' created successfully."

class CreateFullTextIndexCommand:
    """
    Command to create a full-text index on a table in FDDS.
    """

    def __init__(self, engine):
        self.engine = engine

    def execute(self, db_name, table_name, column_name):
        """
        Executes the command to create a full-text index.
        
        :param db_name: The name of the database.
        :param table_name: The name of the table.
        :param column_name: The column to index.
        :return: A confirmation message.
        """
        table = self.engine.get_table(db_name, table_name)
        index = FullTextIndex()
        for row in table.query():
            index.index_document(row["id"], row[column_name])  # Assuming 'id' is the unique identifier
        table.indexes[column_name] = index
        return f"Full-text index on '{column_name}' in table '{table_name}' created successfully."
