# only implemented arithmatic local rules for now

import math

def _ensure_expr(value):
    if isinstance(value,(int, float)):
        return Number(value)
    assert isinstance(value,Expr)
    return value

class Expr:
    type: str
    name: str
    operands: list["Expr"]
    laters: list["Expr"]

    def is_leaf(self):
        return isinstance(self, Number) or isinstance(self, Variable)

    def replace_self(self, new):
        for later in self.laters:
            for i, operand in enumerate(later.operands):
                if operand is self:
                    later.operands[i] = new

    def print_tree(self, indent = 0):
        print(' ' * indent + "└── " + str(self))
        if not self.is_leaf():
            for operand in self.operands:
                operand.print_tree(indent + 4)

    # arithmatic unary
    def __neg__(self):
        return UnaryOp('-', self)
    
    def __pos__(self):
        return UnaryOp('+', self)

    # logical unary
    def __invert__(self):
        return UnaryOp('~', self)

    # arithmatic binary
    def __add__ (self, other):
        return BinaryOp('+',  self, _ensure_expr(other))
    
    def __radd__ (self,other):
        return BinaryOp('+', _ensure_expr(other), self)

    def __sub__(self, other):
        return BinaryOp('-', self, _ensure_expr(other))
    
    def __rsub__(self, other):
        return BinaryOp('-', _ensure_expr(other), self)
    
    def __mul__(self, other):
        return BinaryOp('*', self, _ensure_expr(other))
    
    def __rmul__(self, other):
        return BinaryOp('*', _ensure_expr(other), self)
    
    def __truediv__(self, other):
        return BinaryOp('/', self, _ensure_expr(other))
    
    def __rtruediv__(self, other):
        return BinaryOp('/', _ensure_expr(other), self)

    def __pow__(self, other):  
        return BinaryOp('**', self, _ensure_expr(other))

    def __rpow__(self, other):
        return BinaryOp('**', _ensure_expr(other), self)

    # comparison binary
    def __eq__(self,other):
        return BinaryOp('==',self,_ensure_expr(other))

    def __ne__(self,other):
        return BinaryOp('!=',self,_ensure_expr(other))

    def __lt__(self,other):
        return BinaryOp('<',self,_ensure_expr(other))

    def __le__(self,other):
        return BinaryOp('<=',self,_ensure_expr(other))

    def __gt__(self,other):
        return BinaryOp('>',self,_ensure_expr(other))

    def __ge__(self,other):
        return BinaryOp('>=',self,_ensure_expr(other))

    # logical binary
    def __and__(self,other):
        return BinaryOp('&',self,_ensure_expr(other))

    def __or__(self,other):
        return BinaryOp('|',self,_ensure_expr(other))

    def __xor__(self,other):
        return BinaryOp('^',self,_ensure_expr(other))

    def is_number(self):
        return isinstance(self,Number)

    def is_zero(self):
        return isinstance(self, Number) and abs(self.value) < 1e-12
    
    def is_one(self):
        return isinstance(self, Number) and abs(self.value - 1.0) < 1e-12


    # check if two exprs are structually and valuely identical for cancellation
    def is_same(self, other):
        if type(self) != type(other):
            return False
        if isinstance(self, Number):
            return abs(self.value - other.value) < 1e-12
        elif isinstance(self, Variable):
            return self.name == other.name  
        elif isinstance(self, UnaryOp):
            return (self.operator == other.operator and
                    self.operands[0].is_same(other.operands[0]))
        elif isinstance(self, BinaryOp):
            return (self.operator == other.operator and 
                    self.operands[0].is_same(other.operands[0]) and 
                    self.operands[1].is_same(other.operands[1]))
    
    def _apply_local_rules(self):
        return self
    
class Number(Expr):
    def __init__(self, value):
        self.type = 'number'
        assert isinstance(value,(int,float))
        self.value = float(value)
        self.laters = []

    def __str__(self):
        return str(self.value)
    
class Boolean(Expr):
    def __init__(self, value):
        self.type = 'boolean'
        assert value in (True,False)
        self.value = value
        self.laters = []

    def __str__(self):
        return str(self.value)

class Variable(Expr):
    def __init__(self, name):
        self.type = 'variable'
        self.name = name
        self.laters = []
    
    def __str__(self):
        return str(self.name)


class UnaryOp(Expr):
    def __init__(self, operator: str, operand_A: Expr):
        self.type = 'unaryop'
        assert operator in {'+','-','sin','cos','tan', '~'}
        self.operator = operator
        self.operands = [operand_A]
        operand_A.laters.append(self)
        self.laters = []

    def _apply_local_rules(self):
        operand = self.operands[0]
        if self.operator == '+': return operand
        elif self.operator == '-':
            if operand.is_number(): return Number(-operand.value)
            elif isinstance(operand,UnaryOp) and operand.operator == '-': return operand.operands[0]
        elif self.operator == 'sin' and operand.is_number() : return Number(math.sin(operand.value))
        elif self.operator == 'cos' and operand.is_number() : return Number(math.cos(operand.value))
        elif self.operator == 'tan' and operand.is_number() : return Number(math.tan(operand.value))

    def __str__(self):
        return self.operator


class BinaryOp(Expr):
    def __init__(self, operator, operand_A: Expr, operand_B: Expr):
        self.type = 'binaryop'
        assert operator in {'+','-','*','/','**','log',   #arithmatic
                            '==','!=','<','<=','>','>=',  #conditional
                            '&','|','^'}                  #logical
        self.operator = operator
        self.operands = [operand_A,operand_B]
        operand_A.laters.append(self)
        operand_B.laters.append(self)
        self.laters = []

    def _apply_local_rules(self):
        left, right = self.operands[0], self.operands[1]
        if self.operator == '+':
            if left.is_number() and right.is_number(): return Number(left.value + right.value)
            elif left.is_zero(): return right
            elif right.is_zero(): return left
        if self.operator=='-':
            if left.is_same(right): return Number(0)
            elif left.is_number() and right.is_number(): return Number(left.value - right.value)
            elif left.is_zero(): return UnaryOp('-',right)
            elif right.is_zero(): return left
        if self.operator=='*':
            if left.is_number() and right.is_number(): return Number(left.value * right.value)
            elif left.is_zero(): return Number(0)
            elif right.is_zero(): return Number(0)
            elif left.is_one(): return right
            elif right.is_one(): return left
        if self.operator=='/':
            if right.is_zero(): raise ValueError("division by zero")
            if left.is_number() and right.is_number(): return Number(left.value / right.value)
            elif left.is_same(right): return Number(1)
            elif left.is_zero(): return Number(0)
            elif right.is_one(): return left
        if self.operator=='**':
            if left.is_number() and right.is_number(): return Number(left.value ** right.value)
            elif left.is_zero(): return Number(0)
            elif left.is_one(): return Number(1)
            elif right.is_zero(): return Number(1)
            elif right.is_one(): return left

        return self

    def __str__(self):
        return self.operator

class If(Expr):
    def __init__(self, condition: Expr, if_branch: Expr, else_branch: Expr):
        self.type = 'If'
        self.condition = condition
        self.if_branch = if_branch
        self.else_branch = else_branch
        condition.laters.append(self)
        if_branch.laters.append(self)
        else_branch.laters.append(self)
        self.laters = []

    def print_tree(self, indent = 0):
        print(' ' * indent + "└── " + self.type)
        self.condition.print_tree(indent + 4)
        self.if_branch.print_tree(indent + 4)
        self.else_branch.print_tree(indent + 4)


# class Derivative(Expr):

# class Integral(Expr):

# arithmatic unary functions
def sin(x): return UnaryOp('sin', _ensure_expr(x))
def cos(x): return UnaryOp('cos', _ensure_expr(x))
def tan(x): return UnaryOp('tan', _ensure_expr(x))
# arithmatic binary functions
def log(x,base): return BinaryOp('log', _ensure_expr(x),_ensure_expr(base))


'''
to define complex user functions just use python's normal syntax

i.e.
def foo (x,y,z)
    a = x + y * z
    b = 3 - x ** y
    return a, b
i.e.
def relu(x):
    result = If(x>0, x, Number(0))
    return result
'''



