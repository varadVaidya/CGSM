import numpy as np
from numpy import sin, cos
PI = np.pi
theta = PI/4

x = np.array([
    [4, 2, 1],
    [6, 2, 1],
    [5, 3.732, 1],
])

a = np.array([
    [1, 0, 0],
    [0, 1, 0],
    [0, -2, 1]
])

b = np.array([
    [1, 0, 0],
    [0, -1, 0],
    [0, 0, 1]])

c = np.array([
    [1, 0, 0],
    [0, 3, 0],
    [0, 0, 1]])

d = np.array([
    [1, 0, 0],
    [0, 1, 0],
    [0, 2, 1]
])

# e = np.array([
#     [2, 0, 0],
#     [0, 2, 0],
#     [0, 0, 1]
# ])

# f = np.array([
#     [1, 0, 0],
#     [0, 1, 0],
#     [1, 1, 1]
# ])


# xf = x @ a @ b @ c @ d @ e @ f

print(np.round(a @ b @ c @ d, 3))

print(np.round(x @ a @ b 
@ c @ d, 3))