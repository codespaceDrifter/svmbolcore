from src.symbol import *
from src.simplify import *



x = Variable('x')
y = Variable('y')
z = Variable('z')
exp = Number(3)*4*5
exp.print_tree()

new_exp = exp.simplify()
new_exp.print_tree()
