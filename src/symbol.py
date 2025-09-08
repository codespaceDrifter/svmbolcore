# only implemented arithmatic local rules for now

# TODO: use "variadic operators" with a variable number of operands. plus and mulitplication only. no more minuses and divisions
# TODO: allow forward and backward tracking

import math
from typing import Tuple

class Expr:
    def is_leaf(self):
        return isinstance(self, Number) or isinstance(self, Variable)

    def print_tree(self, indent = 0):
        print(' ' * indent + "└── " + str(self))
        if not self.is_leaf():
            for operand in self.operands:
                operand.print_tree(indent + 4)

    # arithmatic unary
    def __neg__(self): return Mul(-1, self)
    def __pos__(self): return Mul(1, self)
    # arithmatic binary
    def __add__ (self, other): return Add(self, other)   
    def __radd__ (self,other): return Add(other, self)
    def __sub__(self, other): return Add(self,Mul(-1,other))
    def __rsub__(self, other): return Add(other,Mul(-1,self))
    def __mul__(self, other): return Mul(self,other)
    def __rmul__(self, other): return Mul(other,self)   
    def __truediv__(self, other): return Mul(self,Pow(other,-1))
    def __rtruediv__(self, other): return Mul(other,Pow(self,-1))
    def __pow__(self, other):   return Pow(self,other)
    def __rpow__(self, other): return Pow(other,self)
    # comparison binary
    def __eq__(self,other): return Compare('==',self,other)
    def __ne__(self,other): return Compare('!=',self,other)
    def __lt__(self,other): return Compare('<',self,other)
    def __le__(self,other): return Compare('<=',self,other)
    def __gt__(self,other): return Compare('>',self,other)
    def __ge__(self,other): return Compare('>=',self,other)
    # logical unary
    def __invert__(self): return Logic('~', self)
    # logical variadic
    def __and__(self,other): return Logic('&',self,other)
    def __or__(self,other): return Logic('|',self,other)
    def __xor__(self,other): return Logic('^',self,other)
    #helper functions
    def is_number(self): return isinstance(self,Number)
    def is_zero(self): return isinstance(self, Number) and abs(self.value) < 1e-12
    def is_one(self): return isinstance(self, Number) and abs(self.value - 1.0) < 1e-12

def _ensure_expr(value):
    if isinstance(value,(int, float)):
        return Number(value)
    assert isinstance(value,Expr)
    return value

def _as_base_exp(expr):
    assert (isinstance(expr,Expr))
    if isinstance(e,Pow):
        return e.operands[0], e.operands[1]
    return expr, 1

# does not deal with logical ops for now
def canon_key(expr):
    if isinstance(expr, Number):
        return ('NUM', str(expr))
    elif isinstance(expr, Variable):
        return ('VAR', str(expr))
    elif isinstance(expr, Add):
        return ('ADD', tuple(sorted(canon_key(o) for o in expr.operands)))
    elif isinstance(expr, Mul):
        return ('MUL', tuple(sorted(canon_key(o) for o in expr.operands)))
    elif isinstance(expr, Pow):
        return ('POW', tuple(canon_key(o) for o in expr.operands))

    
class Number(Expr):
    def __init__(self, value):
        assert isinstance(value,(int,float))
        self.value = float(value)

    def __str__(self):
        return f"{self.value:.{12}g}"
    
class Boolean(Expr):
    def __init__(self, value):
        super().__init__()
        assert value in (True,False)
        self.value = value

    def __str__(self):
        return str(self.value)

class Variable(Expr):
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return str(self.name)

class Add (Expr):
    def __init__(self, *args):
        ops = []
        for arg in args:
            arg = _ensure_expr(arg)
            if isinstance(arg, Add):
                ops.extend(arg.operands)
            else:
                ops.append(arg)
        ops.sort(key = canon_key)
        self.operands = tuple(ops)

    def __str__(self):
        return '+'
        
    # simplify needs both local rules (i.e. delete 0) and term based simplification
    def simplify(self):
        pass

class Mul (Expr):
    def __init__(self, *args):
        ops = []
        for arg in args:
            arg = _ensure_expr(arg)
            if isinstance(arg, Mul):
                ops.extend(arg.operands)
            else:
                ops.append(arg)
        ops.sort(key = canon_key)
        self.operands = tuple(ops)

    def __str__(self):
        return '*'
    
    def simplify(self):
        pass

class Pow (Expr):
    def __init__ (self, base, exponent):
        self.base = _ensure_expr(base)
        self.exponent = _ensure_expr(exponent)
        self.operands = (self.base, self.exponent)

    def local_rules(self):
        pass

    def __str__(self):
        return '**'

class Compare(Expr):
    def __init__(self, operator, operand_A: Expr, operand_B: Expr):
        assert operator in {'==','!=','<','<=','>','>='} 
        self.operator = operator
        self.operands = (_ensure_expr(operand_A),_ensure_expr(operand_B))

    def __str__(self):
        return self.operator

class Logic(Expr):
    def __init__(self, operator, *args):
        assert operator in {'&','|','^'}                  
        self.operator = operator
        # FIXME: this is wrong perhaps. need to extend things if its a logic of the same operator but fix later
        ops = [_ensure_expr(arg) for arg in args]
        ops.sort(key = canon_key)
        self.operator = tuple(ops) 

    def __str__(self):
        return self.operator

'''

    def _apply_local_rules(self):
        left, right = self.operands[0], self.operands[1]
        if self.operator == '+':
            if left.is_number() and right.is_number(): return Number(left.value + right.value)
            eli left.is_zero(): return right
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
'''

class If(Expr):
    def __init__(self, condition: Expr, if_branch: Expr, else_branch: Expr):
        super().__init__()
        self.type = 'If'
        self.condition = condition
        self.if_branch = if_branch
        self.else_branch = else_branch
        condition.laters.append(self)
        if_branch.laters.append(self)
        else_branch.laters.append(self)

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



