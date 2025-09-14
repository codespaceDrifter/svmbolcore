from src.symbol import *
from src.solve import *

x = Variable('x')
y = Variable('y')

# Parameter (symbolic constant)
a = Variable('a')

eq1 = Eq(2*x + y,a) # = 0
eq2 = Eq(x+y, Number(4))           # = 0

equations = [eq1, eq2]
variables = [x, y]


solutions = solve(equations, variables)
    
print("Solutions:")
for var, sol in solutions.items():
    print(f"{var}")
    sol.print_flat()
