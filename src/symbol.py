# Expr is immutable

import math
from typing import Tuple

class Expr:

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
    def is_leaf(self): return isinstance(self, Number) or isinstance(self, Variable)
    def is_number(self): return isinstance(self,Number)
    def is_zero(self): return isinstance(self, Number) and abs(self.value) < 1e-12
    def is_one(self): return isinstance(self, Number) and abs(self.value - 1.0) < 1e-12

    # assume self is simplified for these _as_sth functions
    def _as_coef_literal(self):
        if isinstance(self, Mul):
            coefficient = Number(1) 
            ops = []
            for operand in self.operands:
                if isinstance(operand, Number):
                    # assume only ONE number exists in operands. assume already simplified
                    coefficient = operand
                else:
                    ops.append(operand)
            return coefficient, Mul(*ops)
        return Number(1), self

    def _as_base_exp(self):
        if isinstance(self,Pow):
            return self.operands[0], self.operands[1]
        return self, Number(1)

    #hash and comparison (same logic)
    def __hash__(self): return hash(canon_key(self))
    def __eq__(self, other):
        if not isinstance(other,Expr):
            return False
        return canon_key(self) == canon_key(other)

    # simplify
    def local_simplify(self):
        return self

    def simplify(self):
        if self.is_leaf():
            return self
        else:
            new_operands = []
            for operand in self.operands:
                new_operand = operand.simplify()
                if new_operand is not None:
                    new_operands.append(new_operand)

            current = type(self)(*new_operands)

            next = current.local_simplify()
            return next

def _ensure_expr(value):
    if isinstance(value,(int, float)):
        return Number(value)
    assert isinstance(value,Expr)
    return value


# does not deal with logical ops for now
# communicative ops' operands are sorted non communicative ops' operand are kept in order
def canon_key(expr):
    if isinstance(expr, Number): return ('NUM', str(expr))
    elif isinstance(expr, Variable): return ('VAR', str(expr))
    elif isinstance(expr, Add): return ('ADD', tuple(sorted(canon_key(o) for o in expr.operands)))
    elif isinstance(expr, Mul): return ('MUL', tuple(sorted(canon_key(o) for o in expr.operands)))
    elif isinstance(expr, Pow): return ('POW', tuple(canon_key(o) for o in expr.operands))

    
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

# local rules: add Numbers. combine same MONOMIAL terms and add their COEFFICIENTS
# special rules. if total is 0 return 0. 
class Add (Expr):
    def __new__(cls, *args):
        constant = 0
        ops = []
        def merge (expr):
            nonlocal constant
            nonlocal ops
            expr = _ensure_expr(expr)
            # add constants directly
            if isinstance(expr,Number):
                constant += expr.value
            else:
                ops.append(expr)
        for arg in args:
            if isinstance(arg, Add):
                for operand in arg.operands:
                    merge(operand)
            else:
                merge(arg)
        constant = Number(constant)
        # if everything is constant(no ops) just return a number
        if len(ops) == 0:
            return constant
        # if constant is not zero add it to ops
        if not constant.is_zero():
            ops.append(constant)
        # if it's just a unary op directly return
        if len(ops) == 1:
            return ops[0]
        ops.sort(key = canon_key)
        add = object.__new__(cls)
        add.operands = tuple(ops)
        return add

    #combine monomial terms
    def local_simplify(self):
        literal_to_coefs = {}
        for operand in self.operands:
            coef, literal = operand._as_coef_literal()

            if literal in literal_to_coefs:
                literal_to_coefs[literal] = literal_to_coefs[literal] + coef
            else:
                literal_to_coefs[literal] = coef

        terms = []
        for literal, coef in literal_to_coefs.items():
            terms.append(coef * literal)

        simplified_terms = []
        for term in terms:
            simplified_term = term.simplify()
            simplified_terms.append(simplified_term)

        return Add (*simplified_terms)


    def __str__(self):
        return '+'
        

# local rules: multiply Numbers. combine same BASES add their EXPONENTS
# special rules: if coefficient is 0, return 0. if coefficient is 1, delete coefficient.
class Mul (Expr):
    def __new__ (cls, *args):
        coefficient = 1
        ops = []
        def merge (expr):
            nonlocal coefficient
            nonlocal ops
            expr = _ensure_expr(expr)
            #multiply numbers directly.
            if isinstance(expr, Number):
                coefficient *= expr.value
            else:
                ops.append(expr)
        for arg in args:
            if isinstance(arg, Mul):
                for operand in arg.operands:
                    merge(operand)
            else:
                merge(arg)
        coefficient = Number(coefficient)
        # if coefficient is 0 return 0
        if coefficient.is_zero():
            return Number(0)
        # if coefficient is 1 delete coefficient
        if not coefficient.is_one():
            ops.append(coefficient)
        # if only one factor just return that
        if len(ops) == 1:
            return ops[0]
        ops.sort(key = canon_key)
        mul =  object.__new__(cls)
        mul.operands = tuple(ops)
        return mul 

    def __str__(self):
        return '*'

    def local_simplify(self):
        # combine operands
        base_to_exps = {}
        for operand in self.operands:
            base, exp = operand._as_base_exp()
            if base in base_to_exps:
                base_to_exps[base] = base_to_exps[base] + exp
            else:
                base_to_exps[base] = exp

        # simplify terms
        factors = []
        for base, exp in base_to_exps.items():
            factors.append(base**exp)
        
        simplified_factors = []
        for factor in factors:
            simplified_factor = factor.simplify()
            simplified_factors.append(simplified_factor)

        result =  Mul (*simplified_factors)
        if isinstance(result, Mul):
            result = result.distribute_add()
        return result
    
    # distribute over add operands. i.e. 3*(a+b) -> 3*a+3*b
    def distribute_add(self) -> Add:
        plus_terms:List[Add] = []
        combine_terms:List[Expr] = []
        for operand in self.operands:
            if isinstance(operand, Add):
                plus_terms.append(operand)
            else:
                combine_terms.append(operand)

        combine_term = Mul(*combine_terms)

        for plus_term in plus_terms:
            new_term = Number(0)
            for plus_op in plus_term.operands:
                new_term = new_term + plus_op * combine_term
            combine_term = new_term.simplify()

        return combine_term


#TODO: special rules: like 0^exp and 1^exp and base^0 and base^1

class Pow (Expr):
    def __new__ (cls, base, exponent):
        base = _ensure_expr(base)
        exponent = _ensure_expr(exponent)
        if base.is_zero():
            if isinstance(exponent, Number):
                assert exponent.value > 0
            return Number(1)
        elif base.is_one():
            return Number(1)
        elif exponent.is_zero():
            return Number(1)
        elif exponent.is_one():
            return base
        elif isinstance(base, Number) and isinstance(exponent, Number):
            return Number(base.value ** exponent.value)

        pow = object.__new__(cls)
        pow.base = base
        pow.exponent = exponent
        pow.operands = (base,exponent)
        return pow

    def local_simplify(self):
        if isinstance(self.base, Pow):
            inner_base = self.base.base
            inner_exponent = self.base.exponent
            new_exponent = self.exponent * inner_exponent
            simplified_exponent = new_exponent.simplify()
            return Pow(inner_base, simplified_exponent)
        return self

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



