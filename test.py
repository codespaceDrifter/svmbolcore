import sys
import os

from svmbolcore.codegen import parse
from svmbolcore.codegen.basics import str_flat
from svmbolcore.codegen.parse import parse_expr

sys.path.append(os.path.join(os.path.dirname(__file__), 'svmbolcore'))

from core.symbol import *
from core.solve import *
from codegen.parse import *
from codegen.basics import *

# Normal add
test_string_0 = "3 + a + b"
expr_0 = parse_expr(test_string_0)
new_string_0 = str_flat(expr_0)
assert new_string_0 == test_string_0

# Normal add with a mul
test_string_1 = "3 + a * b"
expr_1 = parse_expr(test_string_1)
new_string_1 = str_flat(expr_1)
assert new_string_1 == test_string_1

# Normal add with a sub mul
test_string_2 = "a - 5 * b"
expr_2 = parse_expr(test_string_2)
new_string_2 = str_flat(expr_2)
assert new_string_2 == test_string_2

# Normal add with a sub mul and a pow
test_string_3 = "a - 3 * b ** 2"
expr_3 = parse_expr(test_string_3)
new_string_3 = str_flat(expr_3)
assert new_string_3 == test_string_3

# Normal add with a sub mul and a div
test_string_4 = "a - 2 / b"
expr_4 = parse_expr(test_string_4)
new_string_4 = str_flat(expr_4)
assert new_string_4 == test_string_4

# Mul with div in the back (no prefix)
test_string_5 = "b / a"
expr_5 = parse_expr(test_string_5)
new_string_5 = str_flat(expr_5)
assert new_string_5 == test_string_5

# Mul with sub and div
test_string_6 = " - 2 / a"
expr_6 = parse_expr(test_string_6)
new_string_6 = str_flat(expr_6)
assert new_string_6 == test_string_6

# Normal pow
test_string_7 = "a ** 2"
expr_7 = parse_expr(test_string_7)
new_string_7 = str_flat(expr_7)
assert new_string_7 == test_string_7

# Pow with add base and mul exponent (needs parentheses)
test_string_8 = "(a + b) ** (c * d)"
expr_8 = parse_expr(test_string_8)
new_string_8 = str_flat(expr_8)
assert new_string_8 == test_string_8

# Mul with unary minus and div
test_string_9 = " - 5 * a / b"
expr_9 = parse_expr(test_string_9)
new_string_9 = str_flat(expr_9)
assert new_string_9 == test_string_9

# Standalone div (should get 1 prefix)
test_string_10 = " 1 / a"
expr_10 = parse_expr(test_string_10)
new_string_10 = str_flat(expr_10)
assert new_string_10 == test_string_10

# Complex nested case
test_string_11 = "a - 3 * (b + c) ** 2 + d / e"
expr_11 = parse_expr(test_string_11)
new_string_11 = str_flat(expr_11)
assert new_string_11 == test_string_11

# Multiple divisions
test_string_12 = "a / b / c"
expr_12 = parse_expr(test_string_12)
new_string_12 = str_flat(expr_12)
assert new_string_12 == test_string_12

# Unary minus
test_string_13 = " --- a"
expr_13 = parse_expr(test_string_13)
new_string_13 = str_flat(expr_13)
assert new_string_13 == ' - a'

# Equation
test_string_14 = "a + b = c"
expr_14 = parse_expr(test_string_14)
new_string_14 = str_flat(expr_14)
assert new_string_14 == test_string_14

print("PARSING AND PRINTING TEST PASSED")

vars = [
    Variable ('a'),
    Variable ('b')
]
eqs = [
    parse_expr('a + b = 5'),
    parse_expr('a - b = 3')
]
parse_expr('a + b = 5').print_tree()
parse_expr('a - b = 3').print_tree()

sols = solve (eqs, vars)
for k, v in sols.items():
    k.print_tree()
    v.print_tree()
print (sols_to_string_list(sols))
