# import sympy as sy
# from abc import *
# sy.diag(sy.Matrix(0,2,[]),3)+sy.diag(sy.Matrix(2,0,[]))
# sy.Matrix.as_real_imag
# sy.diag(*[3,2,3])

import sympy as sy
# a:sy.Matrix = sy.diag(sy.Matrix(0,2,[]),3,sy.diag(sy.Matrix(2,0,[])))
a:sy.Matrix = sy.Matrix(2,2,[0,3,2,1])
b:sy.Matrix = sy.Matrix(2,2,[2,1,3,0])
b.inv()@a
# print(a)
# print(a.minorMatrix(1,1))
# a.minor()
# a.minor_submatrix()
# a.minorMatrix()


