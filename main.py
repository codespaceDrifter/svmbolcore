import parse

expression = "1 + x - 3 ^ 2 + abc x"

variables = ['x', 'abc', 'def']

expression_list = parse.parse_expression(expression, variables, [])

print([str(expr) for expr in expression_list])
