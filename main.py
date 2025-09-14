from src.symbol import *
from src.solve import *

# TEST CASE 1: Valid solutions (should pass)
x = Variable('x')
y = Variable('y')
z = Variable('z')
expr = x*x*3*y*5 + 2 + 2
expr.print_tree()
expr = expr.simplify()
expr.print_tree()
