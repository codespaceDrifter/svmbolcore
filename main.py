import parse

expression = "5*(a+b)^2+2*a^2+3"

variables = ['a', 'b']

expression_list = parse.parse_expression(expression, variables, [])

new_list = parse.create_AST(expression_list)

new_list[0].print_tree()

