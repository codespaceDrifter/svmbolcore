from src.symbol import *
from src.simplify import *

# TODO: current goal: single Monomial simplification

x = Variable('x')
y = Variable('y')
exp = x**2 * 3 * x + y**3 * y
exp.print_tree()

exp = simplify_tree(exp)
exp.print_tree()

'''
x = Variable('x')
y = Variable('y')
a = x + y
b = a * 2
c = a * 3
d = b + c
d.print_tree()
'''
