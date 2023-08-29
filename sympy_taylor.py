import sympy as sy
from sympy.abc import *
f = sy.ln(z- epsilon)
f.series(x = epsilon)  # 泰勒展开  在这里epsilon 为 x到 x' 的距离，而这里z被看成了x'
sy.diff(sy.ln(x),x,x,x)
# the axis was   from z to 0   

m = (x + sy.I * y)**5
sy.expand(m)
