class Expr:
    def is_leaf(self):
        return isinstance(self, Number) or isinstance(self, Variable)

    def get_precedence(self):
        assert self.is_leaf() == False
        return self.innate_precedence + 5 * self.stack_level


class Number(Expr):
    def __init__(self, value, stack_level = 0):
        self.type = 'number'
        assert value.replace('.','',1).isdigit() and value.count('.') <= 1
        self.value = value
        self.stack_level = stack_level
    
    def print_tree(self, indent = 0):
        print(' ' * indent + "└── " + self.value)

class Variable(Expr):
    def __init__(self, name, stack_level = 0):
        self.type = 'variable'
        self.name = name
        self.stack_level = stack_level
    
    def print_tree(self, indent = 0):
        print(' ' * indent + "└── " + self.name)

class UnaryOp(Expr):
    def __init__(self, operator: str, stack_level = 0):
        self.type = 'unaryop'
        assert operator in {'+','-','sin','cos'}
        self.operator = operator
        self.stack_level = stack_level
        self.left_associative = False;
        self.operands = []
        self.innate_precedence = 3;

    def print_tree(self, indent = 0):
        print(' ' * indent + "└── " + self.operator)
        for operand in self.operands:
            operand.print_tree(indent + 4)

class BinaryOp(Expr):
    def __init__(self, operator, stack_level = 0):
        self.type = 'binaryop'
        assert operator in {'+','-','*','/','^','log'}
        self.operator = operator
        self.stack_level = stack_level
        self.left_associative = True;
        self.operands = []

        if self.operator == '+' or operator == '-':
            self.innate_precedence = 0;
        elif self.operator == '*' or self.operator == '/':
            self.innate_precedence = 1;
        elif self.operator == 'log':
            self.innate_precedence = 2;
        
        # ^ is right associative
        elif self.operator == '^':
            self.innate_precedence = 3;
            self.left_associative = False;

    def print_tree(self, indent = 0):
        print(' ' * indent + "└── " + self.operator)
        for operand in self.operands:
            operand.print_tree(indent + 4)

class Function(Expr):
    def __init__(self, name, stack_level = 0):
        self.type = 'function'
        self.name = name
        self.stack_level = stack_level
        # functions are neither left nor right associative. set to True here to avoid being skipped by parser
        self.left_associative = True;
        self.operands = []
        self.innate_precedence = 4;

    def print_tree(self, indent = 0):
        print(' ' * indent + "└── " + self.name)
        for operand in self.operands:
            operand.print_tree(indent + 4)

# class Derivative(Expr):

# class Integral(Expr):
