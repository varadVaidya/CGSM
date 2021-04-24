import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
#####################################################

t_val = 0.5

pts = [ [2,0,0], [2,3,1], [3,2,2], [4,8,3], [5,3,4], [6,-2,5]]

#####################################################

X = []; Y = []; Z = []
for i in range(len(pts)):
    X.append(pts[i][0])
    Y.append(pts[i][1])
    Z.append(pts[i][2])

n = len(pts) - 1 # degree of bezier curve

#################################################

t = sp.symbols('t')

x_t = 0
y_t = 0
z_t = 0

for i in range(0, n+1):
    x_t += ( X[i] ) * ( sp.factorial(n) / (sp.factorial(i)*sp.factorial(n-i)) ) * ( (t**i) * ( (1-t)**(n-i) ) )
    y_t += ( Y[i] ) * ( sp.factorial(n) / (sp.factorial(i)*sp.factorial(n-i)) ) * ( (t**i) * ( (1-t)**(n-i) ) )
    z_t += ( Z[i] ) * ( sp.factorial(n) / (sp.factorial(i)*sp.factorial(n-i)) ) * ( (t**i) * ( (1-t)**(n-i) ) )

#########################################


print("###########INFO###########")
print('Bezier Poly is')
print('\n\n')
print('======== For X =========')
print('x points i.e [x0, x1,.... xn-1, xn] = ', X)
print('-------------------')
print('x(t) = ', x_t)
print('simplified x(t) = ', sp.simplify(x_t))
print('-------------------')
print('x({}) = '.format(t_val), x_t.subs({t: t_val}))
print('\n\n')
print('======== For Y =========')
print('y points i.e [y0, y1,.... yn-1, yn] = ', Y)
print('-------------------')
print('y(t) = ', y_t)
print('simplified y(t) = ', sp.simplify(y_t))
print('-------------------')
print('y({}) = '.format(t_val), y_t.subs({t: t_val}))
print('\n\n')
print('======== For Z =========')
print('z points i.e [z0, z1,.... zn-1, zn] = ', Z)
print('-------------------')
print('z(t) = ', z_t)
print('simplified z(t) = ', sp.simplify(z_t))
print('-------------------')
print('z({}) = '.format(t_val), z_t.subs({t: t_val}))
print("#########################")

#########################################

time = np.linspace(0, 1, 50)
plot_x = []; plot_y = []; plot_z = []
for i in time:
    plot_x.append(x_t.subs({t: i}))
    plot_y.append(y_t.subs({t: i}))
    plot_z.append(z_t.subs({t: i}))

fig = plt.figure()
ax = plt.axes(projection="3d")

ax.plot3D(plot_x, plot_y, plot_z)
ax.set_box_aspect([1,1,1])

ax.plot3D(X, Y, Z, 'ro')
plt.show()
