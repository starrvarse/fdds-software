# fdds/fdql/expressions.py

class Expression:
    """
    Base class for FDQL expressions.
    """

    def evaluate(self, row):
        """
        Evaluates the expression based on the given row of data.
        
        :param row: The data row to evaluate.
        :return: The result of the expression evaluation.
        """
        raise NotImplementedError("Subclasses must implement the evaluate method.")

class Equals(Expression):
    """
    Expression for checking equality between a column value and a constant.
    """

    def __init__(self, column, value):
        self.column = column
        self.value = value

    def evaluate(self, row):
        return row.get(self.column) == self.value

class GreaterThan(Expression):
    """
    Expression for checking if a column value is greater than a constant.
    """

    def __init__(self, column, value):
        self.column = column
        self.value = value

    def evaluate(self, row):
        return row.get(self.column) > self.value

class And(Expression):
    """
    Expression for logical AND between two expressions.
    """

    def __init__(self, expr1, expr2):
        self.expr1 = expr1
        self.expr2 = expr2

    def evaluate(self, row):
        return self.expr1.evaluate(row) and self.expr2.evaluate(row)

class Or(Expression):
    """
    Expression for logical OR between two expressions.
    """

    def __init__(self, expr1, expr2):
        self.expr1 = expr1
        self.expr2 = expr2

    def evaluate(self, row):
        return self.expr1.evaluate(row) or self.expr2.evaluate(row)
