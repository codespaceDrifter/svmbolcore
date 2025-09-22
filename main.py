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
strs = sols_to_string_list(sols)
assert strs[0] == "b : 1"
assert strs[1] == "a : 4"
print ("PARSE PRINT TESTS PASSED")

