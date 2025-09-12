from src.symbol import *
from src.equation import *


x = Variable('x')
y = Variable('y')
z = Variable('z')

left = 3*x+5
right = 2*x+3

print(f"Type of expr1: {type(left)}")
print(f"Type of expr2: {type(right)}")

eq = Eq(left, right)

eq = eq.simplify()
eq.print_tree()
