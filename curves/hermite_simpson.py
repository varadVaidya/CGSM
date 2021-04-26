import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

#####################################################

u_val = 0.5

pts = [ [1,2,0], [3,4,2]]
tangent_pts = [[2,7,0]]

#####################################################

X = []; Y = []; Z = []
for i in range(len(pts)):
    X.append(pts[i][0])
    Y.append(pts[i][1])
    Z.append(pts[i][2])

#################################################
Boundary_Constraint = np.array([
    [0,0,0,1],
    [1,1,1,1],
    [0,0,1,0],
    [3,2,1,0]
])

Hermite_Matrix = np.array([
    [2,-2,1,1],
    [-3,3,-2,-1],
    [0,0,1,0],
    [1,0,0,0]
])

x_conds = np.array([
    [X[0]],
    [X[1]],
    [tangent_pts[0][0]-X[0]],
    [tangent_pts[0][0]-X[1]]
])

y_conds = np.array([
    [Y[0]],
    [Y[1]],
    [tangent_pts[0][1]-Y[0]],
    [tangent_pts[0][1]-Y[1]]
])

z_conds = np.array([
    [Z[0]],
    [Z[1]],
    [tangent_pts[0][2]-Z[0]],
    [tangent_pts[0][2]-Z[1]]
])

u = sp.symbols('u')
U = sp.Matrix([
    [u**3, u**2, u, 1]
])

#########################################

coeff_x = Hermite_Matrix @ x_conds
coeff_y = Hermite_Matrix @ y_conds
coeff_z = Hermite_Matrix @ z_conds

x_u = U @ coeff_x
y_u = U @ coeff_y
z_u = U @ coeff_z

#########################################
print("###########INFO###########")
print('Hermite Poly is of the form P(u) = a u**3 + b u**2 + c u + d')
print('-------------------')
print('Boundary Constraint Matrix =\n', Boundary_Constraint)
print('-------------------')
print('Hermite Matrix =\n', Hermite_Matrix)
print('\n\n')
print('======== For X =========')
print('coeff_x i.e [a_x, b_x, c_x, d_x] = ', coeff_x.tolist())
print('-------------------')
print('X_conditions i.e [x(0), x(1), x_dot(0), x_dot(1)] = ', x_conds.tolist())
print('-------------------')
print('x(u) = ', x_u.tolist())
print('-------------------')
print('x({}) = '.format(u_val), x_u.subs({u: u_val}).tolist())
print('\n\n')
print('======== For Y =========')
print('coeff_y i.e [a_y, b_y, c_y, d_y] = ', coeff_y.tolist())
print('-------------------')
print('Y_conditions i.e [y(0), y(1), y_dot(0), y_dot(1)] = ', y_conds.tolist())
print('-------------------')
print('y(u) = ', y_u.tolist())
print('-------------------')
print('y({}) = '.format(u_val), y_u.subs({u: u_val}).tolist())
print('\n\n')
print('======== For Z =========')
print('coeff_z i.e [a_z, b_z, c_z, d_z] = ', coeff_z.tolist())
print('-------------------')
print('Z_conditions i.e [z(0), z(1), z_dot(0), z_dot(1)] = ', z_conds.tolist())
print('-------------------')
print('z(u) = ', z_u.tolist())
print('-------------------')
print('z({}) = '.format(u_val), z_u.subs({u: u_val}).tolist())
print('\n\n')
print("#########################")

#######################################

fig = plt.figure()
ax = plt.axes(projection="3d")

u_space = np.linspace(0, 1, 50)
plot_x = []; plot_y = []; plot_z = []
for i in u_space:
    plot_x.append(x_u.subs({u: i}).tolist()[0][0])
    plot_y.append(y_u.subs({u: i}).tolist()[0][0])
    plot_z.append(z_u.subs({u: i}).tolist()[0][0])

ax.plot3D(plot_x, plot_y, plot_z)
ax.set_box_aspect([1,1,1])

ax.plot3D(X, Y, Z, 'ro')

ax.plot3D(tangent_pts[0][0], tangent_pts[0][1], tangent_pts[0][2], 'go')
ax.plot3D([X[0], tangent_pts[0][0]], [Y[0], tangent_pts[0][1]], [Z[0], tangent_pts[0][2]], 'b--')
ax.plot3D([X[1], tangent_pts[0][0]], [Y[1], tangent_pts[0][1]], [Z[1], tangent_pts[0][2]], 'b--')


plt.show()