# fdds/core/transaction_commands.py

class BeginTransactionCommand:
    """
    Command to begin a transaction in FDDS.
    """

    def __init__(self, transaction_manager):
        self.transaction_manager = transaction_manager

    def execute(self, transaction_id):
        """
        Executes the command to begin a new transaction.
        
        :param transaction_id: The unique identifier for the transaction.
        :return: A confirmation message.
        """
        self.transaction_manager.begin_transaction(transaction_id)
        return f"Transaction '{transaction_id}' started successfully."

class CommitTransactionCommand:
    """
    Command to commit a transaction in FDDS.
    """

    def __init__(self, transaction_manager):
        self.transaction_manager = transaction_manager

    def execute(self, transaction_id):
        """
        Executes the command to commit a transaction.
        
        :param transaction_id: The unique identifier for the transaction.
        :return: A confirmation message.
        """
        self.transaction_manager.commit_transaction(transaction_id)
        return f"Transaction '{transaction_id}' committed successfully."

class RollbackTransactionCommand:
    """
    Command to roll back a transaction in FDDS.
    """

    def __init__(self, transaction_manager):
        self.transaction_manager = transaction_manager

    def execute(self, transaction_id):
        """
        Executes the command to roll back a transaction.
        
        :param transaction_id: The unique identifier for the transaction.
        :return: A confirmation message.
        """
        self.transaction_manager.rollback_transaction(transaction_id)
        return f"Transaction '{transaction_id}' rolled back successfully."
