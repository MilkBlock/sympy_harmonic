from sympy import *
m = Matrix(2,2,[0,1,1,1])
print(a1 := m.eigenvects()[0][2][0])
print(b1 := m.eigenvects()[1][2][0])
(c1:=a1.T @ b1).simplify()
print(c1)

m.diagonalize()