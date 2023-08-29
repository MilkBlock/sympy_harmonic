import sympy as sy
from sympy.vector import *
from sympy.abc import *
N= CoordSys3D("N")
r= x* N.i + y *N.j + z*N.k
# divergence(r/r.magnitude()**3)

print(type(r))
delop = Del()
delop.dot(r/r.magnitude()**3)

# v1 = *N.i+4*N.j
# v2 = N.k
# v1^v2
# v1&v2
# from sympy.vector import CoordSys3D
# R = CoordSys3D('R')
# v = 3*R.i + 4*R.j + 5*R.k
# v