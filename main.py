from src.symbol import *
from src.simplify import *



x = Variable('x')
y = Variable('y')
z = Variable('z')

exp = 3 + x**2*4 + 2 * x * x
exp.print_tree()

new_exp = exp.simplify()
new_exp.print_tree()
