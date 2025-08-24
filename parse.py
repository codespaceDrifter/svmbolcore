import symbol

'''
write out all * explicitly, continuous letters will be the name of a single variable
variables and functions need to be PREDEFINED

example usage:
a, b, c = Variable('a'), Variable('b'), Variable('c')
f = Function('f')

expression_one = parse_expression("2.56*x-sin(-y)=5")
'''

# for example: "2.56*x-sin(-y)"

def parse_expression(expression: str, variables: list[str], functions: list[str]) -> list[symbol.Expr]:
    expression_list = []
    expression_length = len(expression)
    i = 0

    # for parsing parentheses
    stack_level = 0

    # for parsing letters
    special_unary = ['sin','cos','tan']
    special_binary = ['log']

    all_named = variables + functions + special_unary + special_binary
    max_named_len = max(len(name) for name in all_named) 

    # if last token is operand, the next + or - is binary
    last_token_is_operator = False

    while i < expression_length:
        char = expression[i]

        if char == ' ' or char == ',':
            pass
        elif char == '(':
            stack_level += 1
        elif char == ')':
            stack_level -= 1

        elif char in {'+','-'}:
            if last_token_is_operator:
                expression_list.append(symbol.UnaryOp(char, stack_level))
            else:
                expression_list.append(symbol.BinaryOp(char, stack_level))
            last_token_is_operator = True

        elif char in {'*','/','^','log'}:
            expression_list.append(symbol.BinaryOp(char, stack_level))
            last_token_is_operator = True

        elif char.isdigit() or char == '.':
            start = i
            while i < expression_length and (expression[i].isdigit() or expression[i] == '.'):
                i += 1
            number_str = expression[start:i]
            expression_list.append(symbol.Number(number_str, stack_level))

            last_token_is_operator = False

            i -= 1

        elif char.isalpha():
            start = i
            matched = None
            for length in range (max_named_len, 0, -1):
                end = min (start + length, expression_length)
                candidate = expression[start:end]
                if candidate in all_named:
                    matched = candidate
                    i = end
                    break

            assert matched != None

            if matched in special_unary:
                expression_list.append(symbol.UnaryOp(matched,stack_level))
                last_token_is_operator = True
            if matched in special_binary:
                expression_list.append(symbol.BinaryOp(matched,stack_level))
                last_token_is_operator = True 
            elif matched in variables:
                if last_token_is_operator == False:
                    last_stack_level = expression_list[-1].stack_level
                    expression_list.append(symbol.BinaryOp('*', last_stack_level))
                expression_list.append(symbol.Variable(matched, stack_level))
                last_token_is_operator = False
            elif matched in functions:
                expression_list.append(symbol.Function(matched, stack_level))
                last_token_is_operator = True
            else:
                raise ValueError(f"Unknown variable or function: {matched}")

            i -= 1
        
        else:
            raise ValueError(f"Unknown character: {char}")

        i += 1

    assert stack_level == 0, "Unbalanced parentheses"

    return expression_list

def create_AST (expression_list: list[symbol.Expr]):


    prescedence_ordering = set()
    for expr in expression_list:
        if expr.is_leaf() == False:
            prescedence_ordering.add(expr.get_precedence())

    sorted_ordering = sorted(prescedence_ordering, reverse = True)

    for cur_prescedence in sorted_ordering:


        # start with all the left associatives and then do the right
        i = 0
        while i < len(expression_list):


            cur_expr = expression_list[i]
            if cur_expr.is_leaf() == False and cur_expr.get_precedence() == cur_prescedence and cur_expr.left_associative == True:
                if cur_expr.type == 'binaryop':

                    cur_expr.operands.append(expression_list[i-1])
                    cur_expr.operands.append(expression_list[i+1])
                    # delete high index to low index to not mess up indexes
                    del expression_list[i+1]
                    del expression_list[i-1]
                    i -= 1

                if cur_expr.type == 'function':
                    function_stack_level = cur_expr.stack_level
                    while expression_list[i+1].is_leaf() == True or expression_list[i+1].stack_level > function_stack_level:
                        cur_expr.operands.append(expression_list[i+1])
                        del expression_list[i+1]

            i += 1

        i = len(expression_list) - 1

        while i >= 0:


            cur_expr = expression_list[i]
            if cur_expr.is_leaf() == False and cur_expr.get_precedence() == cur_prescedence and cur_expr.left_associative == False:
                if cur_expr.type == 'unaryop':
                    cur_expr.operands.append(expression_list[i+1])
                    del expression_list[i+1]
                if cur_expr.type == 'binaryop':
                    cur_expr.operands.append(expression_list[i-1])
                    cur_expr.operands.append(expression_list[i+1])
                    del expression_list[i+1]
                    del expression_list[i-1]
                    i -= 1
            i -= 1
                

    return expression_list
