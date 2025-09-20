from src.symbol import *
from src.solve import *
from codegen.basics import *
import sys
import os

a = Variable('a')
b = Variable('b')
c = Variable('c')
d = Variable('d')


expr = -c ** -1
print(str_flat(expr))
