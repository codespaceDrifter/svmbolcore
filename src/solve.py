import enum
from .symbol import *

#returns an expression that all solvers assume equal to zero
class Eq(Expr):
    def __init__(self, left: Expr, right:Expr = Number(0)):
        self.left = left
        self.right = right
        self.operands = (left,right)

    def __str__(self):
        return '='
    
    def local_simplify(self) -> Expr:
        new_left = self.left - self.right
        simplified_left = new_left.simplify()
        return simplified_left

# assumes expression is simplified
def get_degree(expr):
    max_degree = 0
    def helper(expr):
        nonlocal max_degree
        if isinstance(expr, Pow) and isinstance(expr.base, Variable):
            assert isinstance(expr.exponent, Number) #complex variable exponents not supported yet
            if (expr.exponent.value > max_degree):
                max_degree = expr.exponent.value
        elif expr.is_leaf():
            if isinstance(expr, Variable) and max_degree == 0:
                max_degree = 1
            # if number do nothing
        else:
            for op in expr.operands:
                helper(op)
    helper(expr)
    return max_degree

# no self definition or recurring definitions. i.e. a cant be defined with b and then b defined with a. 
def assert_solutions_valid (solutions: dict[Variable, Expr]):
    # get what variables each solution contains
    def extract_variables(expr):
        contained_vars = set()
        def helper(expr):
            nonlocal contained_vars
            if isinstance(expr, Variable) and expr not in contained_vars:
                contained_vars.add(expr)
            if not expr.is_leaf():
                for op in expr.operands:
                    helper(op)
        helper(expr)
        return contained_vars
    # put solutions into a variable : the variables it's definition contains form
    var_to_defvars = {}
    for var, expr in solutions.items():
        var_to_defvars[var] = extract_variables(expr)

    # while deep traversing along one branch mark as visiting, while finished traversing mark as visited on the function end back up
    # because A->B, and A->D->B is fine but A->B->C and then A->C->B is not (C will lead to B before the recursion calls end and B will still be in visiting so it's A->B->C->B)
    visiting = set()
    visited = set()
    def dfs(var):
        if var in visiting:
            return True
        if var in visited:
            return False
        visiting.add(var)
        for defvar in var_to_defvars[var]:
            if defvar in var_to_defvars:
                if dfs(defvar):
                    return True
        visiting.remove(var)
        visited.add(var)
        return False

    for var in var_to_defvars:
        if var not in visited and dfs(var):
            raise ValueError('cycle definitions')

def subsitute (expr, solutions: dict[Variable,Expr]):
    pass





    


def solve(equation_list:list[Expr], vars:list[Variable]):
    # simplify expressions and change Eqs into expressions
    # assume all expressions is equal to zero
    simplified_list = []
    for e in equation_list:
        simplified_list.append(e.simplify())
    # get max degree of all expressions
    max_degree = 0
    for expr in simplified_list:
        cur_degree = get_degree(expr)
        if cur_degree > max_degree: max_degree = cur_degree
    # send to different solvers
    if max_degree == 1:
        return solve_linear_system(Eq)


def solve_linear(Eq)-> Number:
    pass
    
def solve_quadratic(Eq)-> Number:
    pass

def solve_high_degree(Eq)->Number:
    pass


def solve_linear_system(list)->dict[Variable,Expr]:
    pass












