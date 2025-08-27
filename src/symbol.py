class Expr:
    type: str
    name: str
    operands: list["Expr"]

    def _ensure_expr(self, value):
        if isinstance(value,(int, float)):
            return Number(value)
        assert isinstance(value,Expr)
        return value

    def is_leaf(self):
        return isinstance(self, Number) or isinstance(self, Variable)

    def print_tree(self, indent = 0):
        print(' ' * indent + "└── " + self.name)
        for operand in self.operands:
            operand.print_tree(indent + 4)

    def __add__ (self, other):
        return BinaryOp('+',  self, self._ensure_expr(other))
    
    def __radd__ (self,other):
        return BinaryOp('+', self._ensure_expr(other), self)

    def __sub__(self, other):
        return BinaryOp('-', self, self._ensure_expr(other))
    
    def __rsub__(self, other):
        return BinaryOp('-', self._ensure_expr(other), self)
    
    def __mul__(self, other):
        return BinaryOp('*', self, self._ensure_expr(other))
    
    def __rmul__(self, other):
        return BinaryOp('*', self._ensure_expr(other), self)
    
    def __truediv__(self, other):
        return BinaryOp('/', self, self._ensure_expr(other))
    
    def __rtruediv__(self, other):
        return BinaryOp('/', self._ensure_expr(other), self)

    def __pow__(self, other):  
        return BinaryOp('**', self, self._ensure_expr(other))
    
    def __rpow__(self, other):
        return BinaryOp('**', self._ensure_expr(other), self)
    
    def __neg__(self):
        return UnaryOp('-', self)
    
    def __pos__(self):
        return UnaryOp('+', self)
 


class Number(Expr):
    def __init__(self, value):
        self.type = 'number'
        self.value = value
    
    def print_tree(self, indent = 0):
        print(' ' * indent + "└── " + str(self.value))

class Variable(Expr):
    def __init__(self, name):
        self.type = 'variable'
        self.name = name
    
    def print_tree(self, indent = 0):
        print(' ' * indent + "└── " + self.name)

class UnaryOp(Expr):
    def __init__(self, operator: str, operand_A: Expr):
        self.type = 'unaryop'
        assert operator in {'+','-','sin','cos'}
        self.name = operator
        self.operands = [operand_A]


class BinaryOp(Expr):
    def __init__(self, operator, operand_A: Expr, operand_B: Expr):
        self.type = 'binaryop'
        assert operator in {'+','-','*','/','**','log'}
        self.name = operator
        self.operands = [operand_A,operand_B]


class Function(Expr):
    def __init__(self, name):
        self.type = 'function'
        self.name = name
        # functions are neither left nor right associative. set to True here to avoid being skipped by parser
        self.operands = []


# class Derivative(Expr):

# class Integral(Expr):
