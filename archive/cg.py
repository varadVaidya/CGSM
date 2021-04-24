# import numpy as np

# a = np.array([
#     [0, 0, 0, 1],
#     [1, 1, 1, 1],
#     [0, 0, 1, 0],
#     [3, 2, 1, 0]
# ])

# hi = np.linalg.inv(a)

# # print(ai)

# ax = hi @ np.array([
#     [1],[3],[1],[-1]
# ])

# ay = hi @ np.array([
#     [2],[4],[5],[3]
# ]) 

# # print(ax)

# # print(ay)

# u = 0.8
# u_arr = np.array([[u**3, u**2, u, 1]])

# print(u_arr @ ax)
# print(u_arr @ ay)

import sympy as sp 
# t_val = 0.75
n = 4
t = sp.Symbol('t')
x = 0
ax = [5,6,5,6,7]
for i in range(0,n+1):
    x += ax[i]*sp.factorial(n)*(t**i)*((1-t)**(n-i))/(sp.factorial(i)*sp.factorial(n-i))

print(x)
# print(sp.simplify(x))

# print(x.subs({t: t_val}))

# t_val = 0.75
t = sp.Symbol('t')
y = 0
ay = [4,2,-2,-4,-6]
# ay = []
# for i in range(0,4):
#     ay += [sp.Symbol('B{}'.format(i))]

for i in range(0,n+1):
    y += ay[i]*sp.factorial(n)*(t**i)*((1-t)**(n-i))/(sp.factorial(i)*sp.factorial(n-i))

print(y)
# print(sp.simplify(y))

# print(y.subs({t: t_val}))

t = sp.Symbol('t')
z = 0
az = [2,3,4,3,5]
# ay = []
# for i in range(0,4):
#     ay += [sp.Symbol('B{}'.format(i))]

for i in range(0,n+1):
    z += az[i]*sp.factorial(n)*(t**i)*((1-t)**(n-i))/(sp.factorial(i)*sp.factorial(n-i))

print(z)