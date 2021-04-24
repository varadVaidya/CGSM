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
                [cos(theta), sin(theta), 0],
                [-sin(theta), cos(theta), 0],
                [0, 0, 1]
                ])

    def Trans(self, x, y):
        return np.array([
            [1,0,0],
            [0,1,0],
            [x,y,1],
        ])

    def angle_rotation(self, ref, point, angle):

        T = self.Trans(-ref[0,0], -ref[0,1])
        T_inv = np.linalg.inv(T)

        R_z = self.Rot_z(angle)

        return np.round(point @ (T @ R_z @ T_inv), 3) 

######### User Inputs ############

print("The following script will convert an equilateral triangle TEN into a right angle triangle BEN")
print("-------------------------------------")

E = list(map(float,input("Enter point E[x,y] on the equilateral triangle as a list: ").strip().split()))[:2]
E.append(1)

N = list(map(float,input("Enter point N[x,y] on the same triangle as a list: ").strip().split()))[:2]
N.append(1)

# normal_axis = list(map(float,input("Enter a normal vector (need not be a unit vector) to the plane containing the triangle as a list: ").strip().split()))[:3]
# normal_axis = np.array([normal_axis])
# normal_axis = normal_axis/np.linalg.norm(normal_axis)

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
    T = f.angle_rotation(ref=E, point=N, angle=PI/3)
    B = f.angle_rotation(ref=E, point=T, angle=PI/6)
elif sign == 'cw':
    T = f.angle_rotation(ref=E, point=N, angle=-PI/3)
    B = f.angle_rotation(ref=E, point=T, angle=-PI/6)

####################### Print Info ###################################

print("--------------------------")

s0 = np.sqrt((T[0,0]-N[0,0])**2 + (T[0,1]-N[0,1])**2) # Length of EN
s = np.sqrt((E[0,0]-N[0,0])**2 + (E[0,1]-N[0,1])**2) # Length of EN

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
ax = fig.add_subplot(111, aspect='equal')

ax.set_xlabel('x')
ax.set_ylabel('y')

x1 = [T[0,0],E[0,0],N[0,0],T[0,0]]
y1 = [T[0,1],E[0,1],N[0,1],T[0,1]]
ax.plot(x1, y1, color='blue')

x2 = [B[0,0],E[0,0],N[0,0],B[0,0]]
y2 = [B[0,1],E[0,1],N[0,1],B[0,1]]
ax.plot(x2, y2, color='orange')

ax.text(T[0,0], T[0,1], 'T(' + str(T[0,0]) + ',' + str(T[0,1]) + ')', size=11, zorder=1, color='k')
ax.text(E[0,0], E[0,1], 'E(' + str(E[0,0]) + ',' + str(E[0,1]) + ')', size=11, zorder=1, color='k')
ax.text(N[0,0], N[0,1], 'N(' + str(N[0,0]) + ',' + str(N[0,1]) + ')', size=11, zorder=1, color='k')
ax.text(B[0,0], B[0,1], 'B(' + str(B[0,0]) + ',' + str(B[0,1]) + ')', size=11, zorder=1, color='k')


ax.set_xlim([x1[0] - s, x1[2] + s])
ax.set_ylim([y1[0] - s, y1[2] + s])

plt.show()