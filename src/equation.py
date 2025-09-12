from .symbol import *

class Eq(Expr):
    def __init__(self, left: Expr, right:Expr = Number(0)):
        self.left = left
        self.right = right
        self.operands = (left,right)

    def __str__(self):
        return '='
    
    def local_simplify(self):
        new_left = self.left - self.right
        simplified_left = new_left.simplify()
        return Eq(simplified_left, Number(0))

