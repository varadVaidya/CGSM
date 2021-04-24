""" Write a code to transform an equilateral triangle TEN into right triangle BEN """

import numpy as np 
from numpy import sin, cos 
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

PI = np.pi

######### Helper Class #############

class Transformations:
    def Rot_z(self, theta): 
        return np.array([
                [cos(theta), sin(theta), 0, 0],
                [-sin(theta), cos(theta), 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]
                ])

    def Rot_x(self, theta): 
        return np.array([
                [1, 0, 0, 0],
                [0, cos(theta), sin(theta), 0],
                [0, -sin(theta), cos(theta), 0],
                [0, 0, 0, 1]
                ])

    def Rot_y(self, theta): 
        return np.array([
                [cos(theta), 0, -sin(theta), 0],
                [0, 1, 0, 0],
                [sin(theta), 0, cos(theta), 0],
                [0, 0, 0, 1]
                ])

    def Trans(self, x, y, z):
        return np.array([
            [1,0,0,0],
            [0,1,0,0],
            [0,0,1,0],
            [x,y,z,1],
        ])

    def axis_angle_rotation(self, ref, point, axis, angle):

        # Reference: http://paulbourke.net/geometry/rotate/

        T = self.Trans(-ref[0,0], -ref[0,1], -ref[0,2]).T
        T_inv = np.linalg.inv(T)

        a,b,c = axis[0,0],axis[0,1],axis[0,2]
        d = np.sqrt(b**2 + c**2)

        if d != 0:
            R_x = np.array([
                [1,0,0,0],
                [0,c/d,-b/d,0],
                [0,b/d,c/d,0],
                [0,0,0,1]
                ])
            R_x_inv = R_x.T 
        else:
            R_x = np.identity(4)
            R_x_inv = R_x.T

        R_y = np.array([
            [d,0,-a,0],
            [0,1,0,0],
            [a,0,d,0],
            [0,0,0,1]
            ])
        R_y_inv = R_y.T 

        R_z = self.Rot_z(angle).T

        return np.round( ((T_inv @ R_x_inv @ R_y_inv @ R_z @ R_y @ R_x @ T) @ point.T).T, 3) 
        # return np.round(point @ (T @ R_x @ R_y @ R_z @ R_y_inv @ R_x_inv @ T_inv), 3) 

######### User Inputs ############

print("The following script will convert an equilateral triangle TEN into a right angle triangle BEN")
print("-------------------------------------")

E = list(map(float,input("Enter point E[x,y,z] on the equilateral triangle as a list: ").strip().split()))[:3]
E.append(1)

N = list(map(float,input("Enter point N[x,y,z] on the same triangle as a list: ").strip().split()))[:3]
N.append(1)

normal_axis = list(map(float,input("Enter a normal vector (need not be a unit vector, but should be perpendicular to the line EN)\n to the plane containing the triangle as a list: ").strip().split()))[:3]
normal_axis = np.array([normal_axis])
normal_axis = normal_axis/np.linalg.norm(normal_axis)


while True:
    sign = input('What should be direction of rotation (for converting into a right angle triangle)? \n Enter ccw or cw: ')
    print(sign)
    if (sign != 'ccw') and (sign != 'cw'):
        print("Enter direction again, ccw or cw !!")
    else:
        break
f = Transformations()

N = np.array([N])
E = np.array([E])

###################### Compute T and B ###########################

if sign == 'ccw':
    T = f.axis_angle_rotation(ref=E, point=N, axis=normal_axis, angle=PI/3)
    B = f.axis_angle_rotation(ref=E, point=T, axis=normal_axis, angle=PI/6)
elif sign == 'cw':
    T = f.axis_angle_rotation(ref=E, point=N, axis=normal_axis, angle=-PI/3)
    B = f.axis_angle_rotation(ref=E, point=T, axis=normal_axis, angle=-PI/6)

####################### Print Info ###################################

print("--------------------------")

s0 = np.sqrt((T[0,0]-N[0,0])**2 + (T[0,1]-N[0,1])**2 + (T[0,2]-N[0,2])**2)
s = np.sqrt((E[0,0]-N[0,0])**2 + (E[0,1]-N[0,1])**2 + (E[0,2]-N[0,2])**2)

print('side length', s)
print('side length from generated point', s0)
print('Percentage error in the triangle being equilateral = ', (abs(s-s0)/s)*100)
print('T', T)
print('E', E)
print('N', N)
print('B', B)

############## Plot #####################

fig = plt.figure()
fig.tight_layout()
ax = plt.axes(projection='3d')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

ax.set_aspect('auto')

ax.set_xlim(-s - 2, s + 2)
ax.set_ylim(-s - 2, s + 2)
ax.set_zlim(-s - 2, s + 2)

x1 = [T[0,0],E[0,0],N[0,0]]
y1 = [T[0,1],E[0,1],N[0,1]]
z1 = [T[0,2],E[0,2],N[0,2]]
vertices = [list(zip(x1,y1,z1))]
TEN = Poly3DCollection(vertices, alpha=0.5)
ax.add_collection3d(TEN)

x2 = [B[0,0],E[0,0],N[0,0]]
y2 = [B[0,1],E[0,1],N[0,1]]
z2 = [B[0,2],E[0,2],N[0,2]]
vertices = [list(zip(x2,y2,z2))]
BEN = Poly3DCollection(vertices, alpha=0.8, color='orange')
ax.add_collection3d(BEN)

ax.text(T[0,0], T[0,1], T[0,2], s = 'T(' + str(T[0,0]) + ',' + str(T[0,1]) + ')', size=11, zorder=1, color='k')
ax.text(E[0,0], E[0,1], E[0,2], s = 'E(' + str(E[0,0]) + ',' + str(E[0,1]) + ')', size=11, zorder=1, color='k')
ax.text(N[0,0], N[0,1], N[0,2], s = 'N(' + str(N[0,0]) + ',' + str(N[0,1]) + ')', size=11, zorder=1, color='k')
ax.text(B[0,0], B[0,1], B[0,2], s = 'B(' + str(B[0,0]) + ',' + str(B[0,1]) + ')', size=11, zorder=1, color='k')

plt.show()
