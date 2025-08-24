import parse

expression = "3abab^2+3"

variables = ['a', 'b']

expression_list = parse.parse_expression(expression, variables, [])

new_list = parse.create_AST(expression_list)

new_list[0].print_tree()

