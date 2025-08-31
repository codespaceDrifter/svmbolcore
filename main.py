from src.symbol import *
from src.simplify import *

# TODO: current goal: single Monomial simplification

'''
x = Variable('x')
y = Variable('y')
exp = x**2 * 3 * x + y**3 * y
exp.print_tree()

exp = simplify_tree(exp)
exp.print_tree()
'''

x = Variable('x')
y = Variable('y')
a = x + y
b = a * 2
c = a * 3
d = b + c
d.print_tree()
topo_id_list, get_next  = topo_instance_graph(d, False)

cur_expr, cur_id = topo_id_list[0]
while cur_expr is not None:
    print (f"cur expr {cur_expr} cur id {cur_id}")
    cur_expr,cur_id = get_next(cur_id)



