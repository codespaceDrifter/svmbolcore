import parse

expression = "1 + x - 3 ^ 2 + abc"

variables = ['x', 'abc']

expression_list = parse.parse_expression(expression, variables, [])

print([str(expr) for expr in expression_list])

new_list = parse.create_AST(expression_list)

new_list[0].print_tree()

