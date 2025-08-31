import enum
from .symbol import *

def simplify_tree (expr):
    expr = topo_apply(expr)
    # tree to canonical term list

    # canonical term list addition simplify

    # canonical term list to tree
    return expr

# TODO: have a topo sort method that labels instances and returns a dict of their connections

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


def is_factor(Expr):
    pass


class Monomial(Expr):
    def __init__(self,Expr):


        self.coefficient = 1
        # base and exponent
        self.factors: list[tuple[Expr,Expr]] = []

    def absorb(self, Expr):
        pass
        


#class Polynomial():

