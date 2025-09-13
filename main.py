from src.symbol import *
from src.solve import *

# TEST CASE 1: Valid solutions (should pass)
x = Variable('x')
y = Variable('y')
z = Variable('z')

expr = x*y*5*z**3
print(get_degree(expr))
