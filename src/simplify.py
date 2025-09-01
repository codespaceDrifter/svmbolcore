import enum
from .symbol import *

def simplify_tree (expr):
    expr = topo_apply(expr)
    topo_id_list, get_next = topo_instance_graph(Expr)
    return expr


# topo sorts the tree and assigns an id to each unique instance 
# returns a list of the sorted (expr, int) 
# and returns a function of the id to the next (next is opposite of operand) tuple
def topo_instance_graph(expr, debug = False):
    topo_list : list[Expr] = []
    # ordered. 1 to 1 correspondence with topo list
    topo_id_list: list[tuple[Expr,int]] = []
    id_forwards: Dict[int: int] = {}
    id = 0
    def topo_helper(expr,caller_id = -1):
        nonlocal id
        nonlocal id_forwards
        cur_id = id
        #print(f"cur id {cur_id}, caller id, {caller_id}, expr {expr}")
        id += 1
        if not expr.is_leaf():
            for operand in expr.operands:
                topo_helper(operand, cur_id)
        topo_id_list.append((expr,cur_id))
        id_forwards[cur_id] = caller_id

    topo_helper(expr)

    if debug == True:
        print("topo id list")
        for curexpr, curid in topo_id_list:
            print(curexpr, curid)
        print("forward dict")
        print (id_forwards)

    id_to_topo: Dict[int: Expr] = {curid: curexpr for curexpr,curid in topo_id_list}

    def get_next(id) -> tuple[Expr,int]:
        next_id = id_forwards[id]
        if (next_id == -1):
            return None, None
        next_topo = id_to_topo[next_id]
        return next_topo,next_id 

    return topo_id_list, get_next 

def topo_apply(expr):
    if not expr.is_leaf():
        for i, operand in enumerate(expr.operands):
            expr.operands[i] = topo_apply(operand)
    return expr._apply_local_rules()

# simplify a single multiplication chain: 3*a*b
# simplify a multiplication chain with powers i.e. 3*a^2*b^3
# simplify a chain with other interrupts i.e. 3+a^2*b
class Monomial(Expr):
    def __init__(self):
        self.coefficient = 1
        # base and exponent
        self.factors: Dict[Expr: Expr]= {} 
    
    def absorb(self, expr):
        if isinstance(expr,Number):
            self.coefficient *= Expr
        if isinstance(expr,Variable):
            self.factors[expr] = self.factors[expr] + 1
        if isinstance(expr,BinaryOp) and expr.operator=='*':
            self.factors[expr.operands[0]] = self.factors[expr.operands[0]] + 

        


#class Polynomial():

