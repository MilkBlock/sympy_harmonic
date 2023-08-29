import sympy as sy
from sympy.abc import *
f:sy.Symbol = m*n
k1,k2 = sy.symbols("k1 k2")
g = (m-k1)*(n-k2)
(f-g).expand().simplify()

sy.