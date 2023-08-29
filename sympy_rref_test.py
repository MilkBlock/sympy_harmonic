from sympy import *
from sympy.abc import *

m:Matrix = Matrix([3,2,5,2,0,1,2,4,5]).reshape(3,3)
# print(m)
# print(m.lower_triangular())
# print(m.rref())
m.berkowitz()
