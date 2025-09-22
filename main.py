import sys
import os

from svmbolcore.codegen.basics import str_flat
from svmbolcore.codegen.parse import parse_expr

sys.path.append(os.path.join(os.path.dirname(__file__), 'svmbolcore'))

from core.symbol import *
from core.solve import *
from codegen.parse import *
from codegen.basics import *

# from svmbolcore import *

expr = parse_expr(" a * - c *b**-1")
print (str_flat(expr))
