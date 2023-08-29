from sympy.abc import x,y,z,rho,theta
import sympy as sy
from sympy import integrate,sqrt,cos,pi,sin
from sympy import Matrix,atan2,atan,tan
from sympy.physics.vector import *

N:ReferenceFrame = sy.symbols("N" , cls = ReferenceFrame)
q1 = sy.symbols("q1")
A = N.orientnew("A","Axis",[q1, N.x ])
print(A.dcm(N))

a = integrate(rho**3 , (rho,0,2*cos(theta)))
print(a)
b = integrate(a, (theta,0,pi/2))
print("type1:",b)
a = integrate((1+rho*cos(theta))**2  +  (rho*sin(theta))**2, (rho,0,1))
print( a )
b = integrate(a, (theta,0,pi))
print("type1:",b)

s = Matrix([[0,3,2],[2,0,6],[0,5,0]])
print(s)
s.inv()
print(s.col(0))


N = ReferenceFrame('N')
u1, u2 = dynamicsymbols('u1 u2')  # default to be the function of time 
q1, q2 = dynamicsymbols('q1 q2')  
l , R = sy.symbols("l R")
C = N.orientnew('C', 'Axis', [q1, N.x])  # the orientation of the N has tur to 
C.set_ang_vel(N, u1 * N.x)  # angle velocity velocity velcoity velocity locit locity  locity locity velocity ocity locity rect velocity city city city city rectification       
O = Point('O')
# rectification    vel vel vel vedal vedal vedal vedal vedal ve ve velocity velocity velocity velocity velocity thrust thrust thrust thrust thrust thrust thrsut thrsut thrust thrust thrust thrust thrust 
# modification modification modification odifictation cation odification modi modi modi modi odi modi modi modi tsudu tsudu tsudu studtsd  tsu tsudu tsudu tsudu tsudu 

O.set_vel(N, 0)
Q = O.locatenew('Q', -l * C.z)
P = Q.locatenew('P', R * (cos(q2) * C.x + sin(q2) * C.y))
P.set_vel(C, R * u2 * (-sin(q2) * C.x + cos(q2) * C.y))
Q.v2pt_theory(O, N, C)
P.v1pt_theory(Q, N, C)

# from functools import reduce
# reduce(lambda x,y:x+y, [3,2,3])

# from sympy.vector import CoordSys3D
# ",".join()
# N = CoordSys3D("N")
# C = N.i+N.j + N.j
# # C