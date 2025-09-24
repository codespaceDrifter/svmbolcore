from svmbolcore import *

vars = [
    Variable ('a'),
    Variable ('b')
]
eqs = [
    parse_expr('a + b = 5'),
    parse_expr('a - b = 3')
]

sols = solve(eqs, vars)

solstrs = sols_to_string_list(sols)
for solstr in solstrs:
    print(solstr)
