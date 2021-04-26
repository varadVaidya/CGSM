import numpy as np
from numpy import sin, cos

Trans = lambda x,y,z: np.array([
                        [1, 0, 0, 0],
                        [0, 1, 0, 0],
                        [0, 0, 1, 0],
                        [x, y, z, 1],
                    ])

Scale = lambda x,y,z: np.array([
                        [x, 0, 0, 0],
                        [0, y, 0, 0],
                        [0, 0, z, 0],
                        [0, 0, 0, 1],
                    ])

Rotz = lambda theta: np.array([
                        [ cos(theta), sin(theta), 0, 0],
                        [-sin(theta), cos(theta), 0, 0],
                        [          0,          0, 1, 0],
                        [          0,          0, 0, 1],
                    ])

Rotx = lambda theta: np.array([
                        [1,           0,          0, 0],
                        [0,  cos(theta), sin(theta), 0],
                        [0, -sin(theta), cos(theta), 0],
                        [0,           0,          0, 1],
                    ])

Roty = lambda theta: np.array([
                        [ cos(theta), 0, -sin(theta), 0],
                        [          0, 1,           0, 0],
                        [ sin(theta), 0,  cos(theta), 0],
                        [          0, 0,           0, 1],
                    ])

Shear = lambda x,y,z: np.array([
                        [1, y, z, 0],
                        [x, 1, z, 0],
                        [x, y, 1, 0],
                        [0, 0, 0, 1],
                    ])

Refx = np.array([
            [ -1,  0, 0, 0],
            [  0,  1, 0, 0],
            [  0,  0, 1, 0],
            [  0,  0, 0, 1]
        ])

Refz = np.array([
            [  1,  0,  0, 0],
            [  0,  1,  0, 0],
            [  0,  0, -1, 0],
            [  0,  0,  0, 1]
        ])

Refy = np.array([
            [  1,  0, 0, 0],
            [  0, -1, 0, 0],
            [  0,  0, 1, 0],
            [  0,  0, 0, 1]
        ])

th = np.pi * 45 / 180
axis = np.array([[1,1,1]])
norm_ax = np.linalg.norm(axis)
B = np.arccos(axis[0,1]/norm_ax)
C = np.arccos(axis[0,2]/norm_ax)

T = np.round(Roty(B) @ Rotz(-C) @ Rotx(th) @ Rotz(C) @ Roty(-B), 3)

print(T)

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

    def axis_angle_rotation(self, ref, axis, angle):

        # Reference: http://paulbourke.net/geometry/rotate/

        T = self.Trans(-ref[0,0], -ref[0,1], -ref[0,2])
        T_inv = np.linalg.inv(T)

        norm_axis = np.linalg.norm(axis)
        axis = axis/norm_axis

        a,b,c = axis[0,0],axis[0,1],axis[0,2]
        d = np.sqrt(b**2 + c**2)

        if d != 0:
            R_x = np.array([
                [1,0,0,0],
                [0,c/d,b/d,0],
                [0,-b/d,c/d,0],
                [0,0,0,1]
                ])
            R_x_inv = R_x.T 
        else:
            R_x = np.identity(4)
            R_x_inv = R_x.T

        R_y = np.array([
            [d,0,a,0],
            [0,1,0,0],
            [-a,0,d,0],
            [0,0,0,1]
            ])
        R_y_inv = R_y.T 

        R_z = self.Rot_z(angle)

        return np.round( (T @ R_x @ R_y @ R_z @ R_y_inv @ R_x_inv @ T_inv), 3) 

f = Transformations()

ref = np.array([[0,0,0,1]])

axis = np.array([[1,1,1]])

angle = th

T = f.axis_angle_rotation(ref, axis, angle)

print(T)