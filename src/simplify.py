
from .symbol import *

def simplify_tree (Expr):
    Expr = topo_apply(Expr)
    # tree to canonical term list

    # canonical term list addition simplify

    # canonical term list to tree
    return Expr

def topo_apply(Expr):
    if not Expr.is_leaf():
        for i, operand in enumerate(Expr.operands):
            Expr.operands[i] = topo_apply(operand)
    return Expr._apply_local_rules()

#def collect_polynomial_term(Expr):

class Monomial(Expr):
    def __init__(self):
        self.coefficient = 1
        # base and exponent
        self.factors: list[tuple[Expr,Expr]] = []

    def absorb(self, Expr):
        


#class Polynomial():
