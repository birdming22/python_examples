"""strategy function example
ref. https://stackoverflow.com/questions/963965/how-to-write-strategy-pattern-in-python-differently-than-example-in-wikipedia
"""

def strategy_add(op1, op2):
    """strategy add"""
    return op1 + op2

def strategy_sub(op1, op2):
    """strategy sub"""
    return op1 - op2

SOLVER = strategy_add
print SOLVER(2, 1)
SOLVER = strategy_sub
print SOLVER(2, 1)
