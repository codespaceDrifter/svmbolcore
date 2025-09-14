import enum
from .symbol import *

#returns an expression that all solvers assume equal to zero
class Eq(Expr):
    def __init__(self, left: Expr, right:Expr = Number(0)):
        self.left = left
        self.right = right
        self.operands = (left,right)
        self.simplified = False

    def __str__(self):
        return '='
    
    def local_simplify(self) -> Expr:
        simplified_left = self.left.simplify()
        simplified_right = self.right.simplify()
        result = Eq(simplified_left,simplified_right)
        result.simplified = True
        return result

    def to_expr(self) -> Expr:
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
        e = e.simplify()
        if isinstance(e, Eq):
            simplified_list.append(e.to_expr())
        else:
            simplified_list.append(e)
    # get max degree of all expressions
    max_degree = 0
    for expr in simplified_list:
        cur_degree = get_degree(expr)
        if cur_degree > max_degree: max_degree = cur_degree
    # send to different solvers
    if max_degree == 1:
        return solve_linear_system(simplified_list, vars)

# i.e. 3*a + b + 5 solve for a
# Add: find terms with a, minus both sides with it
# Mul: find non a terms, divide both 
def solve_linear_system(exprs: list[Expr], vars: list[Variable])->dict[Variable,Expr]:
    num_exprs = len(exprs)
    num_vars = len(vars)
    assert (num_exprs == num_vars)
    #assume the expr is one degree max. therefore no pow. 
    # TODO: change helpers to allow like parameters as coefficients so a*b * x is solvable
    def extract_number_coef(expr, var):
        terms = expr._as_add_terms()
        for term in terms:
            coef, literal = term._as_coef_literal()
            if var == literal:
                assert isinstance(coef,Number)
                return coef
        return Number(0)
    # gets the parameters and constant and negates it
    def extract_neg_constant_parameters(expr):
        terms = expr._as_add_terms()
        neg = Number(0)
        for term in terms:
            coef, literal = term._as_coef_literal() # numbers have literal 1 which is not in vars
            if literal not in vars:
                neg = neg - term
        return neg
    # augmented matrix of Ax = -b. constant is negative
    matrix = []
    for expr in exprs:
        row = []
        for var in vars:
            row.append(extract_number_coef(expr,var))
        row.append(extract_neg_constant_parameters(expr))
        matrix.append(row)


    def find_pivot_row(matrix, col):
        num_rows = len(matrix)
        for i in range (col, num_rows):
            if not matrix[i][col].is_zero():
                return i
        raise ValueError('infinite solutions not supported yet')
    for i in range(num_exprs):
        pivot_row = find_pivot_row(matrix, i)
        matrix[i], matrix[pivot_row] = matrix[pivot_row], matrix[i]
        pivot = matrix[i][i]
        assert not pivot.is_zero()
        for j in range (i+1, num_exprs):
            factor = matrix[j][i] / pivot
            for k in range (i, num_exprs + 1): # because one additional const column
                matrix[j][k] = matrix[j][k] - matrix[i][k] * factor
    solutions = {}
    # start at the last row 2nd last col. go diagnolly upwards
    # minus augmented row with coef * solution[var] of latter cols
    for i in range (num_exprs -1, -1, -1):
        value = matrix[i][-1]
        for j in range (num_exprs - 1, i, -1): #2nd last col to after current col
            coef_solution = matrix[i][j]
            literal_solution = solutions[vars[j]]
            value = value - coef_solution * literal_solution
        coef = matrix[i][i]
        sol = (value / coef).simplify()
        solutions[vars[i]] = sol
    return solutions


#TODO: do NOT do quadratic system. just do single equation. no time for now. 
def solve_quadratic(expr, var)-> Number:
    pass

