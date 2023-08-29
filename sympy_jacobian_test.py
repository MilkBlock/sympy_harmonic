from sympy.abc import *
import sympy as sy
from sympy import sin,cos,Matrix
# 球面坐标求取
x = rho*sin(phi)*cos(theta)
y = rho*sin(phi)*sin(theta)
z = rho*cos(phi)

a :Matrix = sy.Matrix([x,y,z])
b :Matrix = sy.Matrix([rho,phi,theta])

a.jacobian(b).det().simplify()

# 极坐标求取
# x = rho*cos[theta]
# y = rho*sin(theta)
# a :Matrix = sy.Matrix([x,y])
# b :Matrix = sy.Matrix([rho,theta])

# a.jacobian(b).det().simplify()


