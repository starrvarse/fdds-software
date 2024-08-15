# fdds/core/concurrency.py

import threading
import copy

class MVCCManager:
    """
    Manages Multi-Version Concurrency Control (MVCC) for FDDS.
    """

    def __init__(self):
        self.lock = threading.Lock()
        self.versions = {}  # Stores versions of tables

    def begin_transaction(self, table):
        """
        Begins a new transaction by taking a snapshot of the table.
        
        :param table: The table object to snapshot.
        :return: A snapshot of the table.
        """
        with self.lock:
            version = copy.deepcopy(table)
            self.versions[id(version)] = version
            return version

    def commit_transaction(self, table, transaction_id):
        """
        Commits a transaction by merging the changes into the main table.
        
        :param table: The original table object.
        :param transaction_id: The ID of the transaction to commit.
        """
        with self.lock:
            if transaction_id in self.versions:
                table.rows = self.versions[transaction_id].rows
                del self.versions[transaction_id]

    def rollback_transaction(self, transaction_id):
        """
        Rolls back a transaction by discarding its changes.
        
        :param transaction_id: The ID of the transaction to roll back.
        """
        with self.lock:
            if transaction_id in self.versions:
                del self.versions[transaction_id]
