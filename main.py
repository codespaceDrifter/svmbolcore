from src.symbol import *
from src.simplify import *



x = Variable('x')
y = Variable('y')
z = Variable('z')
exp = x + y + x*y*z**2 
exp.print_tree()

