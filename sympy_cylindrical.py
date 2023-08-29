from sympy.abc import *
from sympy.vector import *
import sympy as sy
# x = rho *sy.cos(theta)
# y = rho *sy.sin(theta)
# z = sy.sin(theta)
# y = sy.sin(theta)
# C = CoordSys3D("C",transformation="spherical")
C = CoordSys3D("C",transformation="cylindrical")
# coordinate system 3d
v = x*C.i + y*C.j + z*C.k
# define a vector which has 3 components x 
# y z with there directions  i j k
f = sy.symbols("f",cls=sy.Function)
# define a function f 
sfield = f(v)
# indicate that sfield is a scalar 
# field(as the output of f) with  v(a vector) as input
type(sfield)
# sfield
delop:Vector. = Del()  # define del operator(nabla) 
# m  = delop.gradient(v)  
# print(sy.latex(m))
# m
delop.

# sy.integrate(sy.integrate(delop.dot(v/v.magnitude()**2),(x,-sy.oo,+sy.oo)),(y,-sy.oo,+sy.oo))
# use del operator to calculate the gradient of sfield 

