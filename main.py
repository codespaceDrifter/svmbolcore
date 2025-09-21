'''
import sys
import os

from svmbolcore.codegen.parse import parse_expr

sys.path.append(os.path.join(os.path.dirname(__file__), 'svmbolcore'))

from core.symbol import *
from core.solve import *
from codegen.parse import *
from codegen.basics import *

'''
from svmbolcore import *

expr = parse_expr("((a+b)*c)**((d-e)/f) = 5")
expr.print_flat()
