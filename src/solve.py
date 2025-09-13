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
    if isinstance(expr, Number):
        return 0
    elif isinstance(expr, Variable):
        return 1
    elif isinstance(expr, Pow) and isinstance(expr.base, Variable):
        assert isinstance(expr.exponent, Number), "Complex variable exponents not supported yet"
        return int(expr.exponent.value)
    elif isinstance(expr, Mul):
        total_degree = 0
        for operand in expr.operands:
            total_degree += get_degree(operand)
        return total_degree
    elif isinstance(expr, Add):
        max_degree = 0
        for operand in expr.operands:
            operand_degree = get_degree(operand)
            if operand_degree > max_degree:
                max_degree = operand_degree
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
    assert_solutions_valid(solutions)
    def helper(expr):
        if expr in solutions:
            return solutions[expr]
        elif expr.is_leaf():
            return expr
        else:
            new_operands = []
            for op in expr.operands:
                new_op = helper(op)
                new_operands.append(new_op)
            return type(expr)(*new_operands)
    cur = expr
    while True:
        next = helper(cur)
        if next == cur:
            break
        cur = next
    return cur


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
        return solve_linear_system(simplified_list, vars)


def solve_linear(expr, var)-> Number:
    pass

def solve_linear_system(exprs, vars)->dict[Variable,Expr]:
    pass
    
def solve_quadratic(expr, var)-> Number:
    pass

