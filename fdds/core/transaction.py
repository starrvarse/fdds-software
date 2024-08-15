# fdds/core/transaction.py

class TransactionManager:
    """
    Manages transactions in FDDS, ensuring ACID properties: Atomicity, Consistency, Isolation, and Durability.
    """

    def __init__(self):
        self.active_transactions = {}

    def begin_transaction(self, transaction_id):
        """
        Begins a new transaction.
        
        :param transaction_id: A unique identifier for the transaction.
        """
        if transaction_id in self.active_transactions:
            raise ValueError(f"Transaction '{transaction_id}' is already active.")
        self.active_transactions[transaction_id] = []

    def commit_transaction(self, transaction_id):
        """
        Commits the active transaction, applying all changes.
        
        :param transaction_id: The identifier of the transaction to commit.
        """
        if transaction_id not in self.active_transactions:
            raise ValueError(f"No active transaction with id '{transaction_id}'.")
        # Apply all operations in the transaction log
        for operation in self.active_transactions[transaction_id]:
            operation.apply()
        del self.active_transactions[transaction_id]

    def rollback_transaction(self, transaction_id):
        """
        Rolls back the active transaction, discarding all changes.
        
        :param transaction_id: The identifier of the transaction to roll back.
        """
        if transaction_id not in self.active_transactions:
            raise ValueError(f"No active transaction with id '{transaction_id}'.")
        # Discard all operations in the transaction log
        del self.active_transactions[transaction_id]

    def log_operation(self, transaction_id, operation):
        """
        Logs an operation in the active transaction's log.
        
        :param transaction_id: The identifier of the active transaction.
        :param operation: The operation to log.
        """
        if transaction_id not in self.active_transactions:
            raise ValueError(f"No active transaction with id '{transaction_id}'.")
        self.active_transactions[transaction_id].append(operation)
