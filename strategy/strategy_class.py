"""strategy Example
ref. https://sourcemaking.com/design_patterns/strategy/python/1
"""

class StrategyExample(object):
    """Strategy Example class"""

    def __init__(self):
        self.op1 = 0
        self.op2 = 0
        self.result = 0
        self.operation = ""

    def operate(self, op1, op2):
        """operate"""
        self.op1 = op1
        self.op2 = op2

    def print_result(self):
        """print result"""
        print self.op1, self.operation, self.op2, '=', self.result

class AddStrategy(StrategyExample):
    """Implement add operation"""

    def __init__(self):
        super(AddStrategy, self).__init__()
        self.operation = "+"

    def operate(self, op1, op2):
        """operate"""
        super(AddStrategy, self).operate(op1, op2)
        self.result = op1 + op2

class SubStrategy(StrategyExample):
    """Implement sub operation"""

    def __init__(self):
        super(SubStrategy, self).__init__()
        self.operation = "-"

    def operate(self, op1, op2):
        """operate"""
        super(SubStrategy, self).operate(op1, op2)
        self.result = op1 - op2


if __name__ == '__main__':
    SOLVER = AddStrategy()
    SOLVER.operate(2, 1)
    SOLVER.print_result()
    SOLVER = SubStrategy()
    SOLVER.operate(2, 1)
    SOLVER.print_result()
