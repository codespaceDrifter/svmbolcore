class Expr:

    def is_leaf(self):
        return isinstance(self, Number) or isinstance(self, Variable)

    def get_precedence(self):
        assert self.is_leaf() == False
        return self.precedence + 5 * self.stack_level

    def __str__(self): pass

class Number(Expr):
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return self.value

class Variable(Expr):
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name

class UnaryOp(Expr):
    def __init__(self, operator: str, stack_level = 0):
        assert operator in {'+','-','sin','cos'}
        self.left_associative = False;
        self.operator = operator
        self.operand = None
        self.precedence = 3;
        self.stack_level = stack_level

    def __str__(self):
        return self.operator

class BinaryOp(Expr):
    def __init__(self, operator, stack_level = 0):
        assert operator in {'+','-','*','/','^','log'}
        self.left_associative = True;
        self.operator = operator
        self.left_operand = None
        self.right_operand = None
        self.stack_level = stack_level

        if self.operator == '+' or operator == '-':
            self.precedence = 0;
        elif self.operator == '*' or self.operator == '/':
            self.precedence = 1;
        elif self.operator == 'log':
            self.precedence = 2;
        
        # ^ is right associative
        elif self.operator == '^':
            self.precedence = 3;
            self.left_associative = False;

    def __str__(self):
        return self.operator

class Function(Expr):
    def __init__(self, name, stack_level = 0):
        self.name = name
        self.arguments = []
        self.stack_level = stack_level
        self.precedence = 4;

    def __str__(self):
        return self.name

# class Derivative(Expr):

# class Integral(Expr):

