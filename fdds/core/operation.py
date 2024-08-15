# fdds/core/operation.py

class Operation:
    """
    Represents a reversible operation within a transaction.
    """

    def __init__(self, apply_func, rollback_func):
        """
        Initializes an operation with apply and rollback functions.
        
        :param apply_func: The function to apply the operation.
        :param rollback_func: The function to rollback the operation.
        """
        self.apply_func = apply_func
        self.rollback_func = rollback_func

    def apply(self):
        """
        Applies the operation.
        """
        self.apply_func()

    def rollback(self):
        """
        Rolls back the operation.
        """
        self.rollback_func()
