from svmbolcore import *

expr = parse_expr(" a + b = 5")
expr.print_tree()
print(str_flat(expr))
