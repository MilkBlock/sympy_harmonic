# from sympy.abc import *
import sympy as sy
a,a1,a2,v1,v2,v3,m,n,t1,t2,t = sy.symbols("a a1 a2 v1 v2 v3 m n t1 t2 t")
t1 = (0.5+ 0 )/ 2  # a1 所在的时间点
t2 = (0.75+ 0.5 )/ 2
a = m*t + n 
a1 = (v2-v1)/(0.5)
a2 = (v3-v2)/(0.25)
# m = (a2-a1)/(t2-t1)
solution =  sy.solve([sy.Equality(a1,m*t1+n),sy.Equality(a2,m*t2+n),],[m,n])
# print(sy.integrate(a,(t,0,1)))
# print(m,n)
x:sy.Symbol = sy.integrate(sy.integrate(a,(t,0,t))+v1 ,(t,0,1))
print(a.integrate((t,0,t)).integrate((t,0,1)))
# print(x.evalf(subs=solution))


# m = a1()



