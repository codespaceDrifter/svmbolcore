from src.symbol import *

'''
x = Variable('x')
z = x**2 + 2*x**2 + x + 5*x + 3+4
z.print_tree()
'''

a = Number(4) + Number(5)
a.print_tree()
a = a._apply_local_rules()
a.print_tree()


