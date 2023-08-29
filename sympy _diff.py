from sympy.abc import *
import sympy as sy
f:sy.Symbol = 3*x*y + 4*x**2 + 5*y**2 + 1/y + x+x + sy.E**(x*y)

print(sy.srepr(f))
print(f.func)
f.func(*f.args)
print(f.args[2].args)
print("the derivative of x&y is:")
print(sy.diff(f,x,y))
print(sy.diff(f,y,x))

# sy.laplace_transform()

print(sy.integrate(1/(1-x**4)),(x))
print(sy.latex(sy.integrate(x+sy.ln(x))))



sy.integrate(sy.sec(x),x).simplify()



