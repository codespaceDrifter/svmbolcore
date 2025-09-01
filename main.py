from src.symbol import *
from src.simplify import *



# TODO: current goal: single Monomial simplification

'''
x = Variable('x')
y = Variable('y')
exp = x**2 * 3 * x + y**3 * y
exp.print_tree()

exp = simplify_tree(exp)
exp.print_tree()
'''

a = Variable('a')
b = Variable('b')
exp = 3*a*b
exp.print_tree()
