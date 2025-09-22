from svmbolcore import *

vars = [
    Variable ('a')
    Variable ('b')
]
eqs = [
    Eq ( a + b = 5)
    Eq ( a - b = 3)

]


sols = solve (eqs, vars)

print (sols_to_string_list(sols))
