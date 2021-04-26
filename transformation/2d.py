import numpy as np
from numpy import sin, cos

Trans = lambda x,y: np.array([
                        [1, 0, 0],
                        [0, 1, 0],
                        [x, y, 1]
                    ])

Scale = lambda x,y: np.array([
                        [x, 0, 0],
                        [0, y, 0],
                        [0, 0, 1]
                    ])

Rotn = lambda theta: np.array([
                        [ cos(theta), sin(theta), 0],
                        [-sin(theta), cos(theta), 0],
                        [          0,          0, 1]
                    ])

Shear = lambda x,y: np.array([
                        [1, y, 0],
                        [x, 1, 0],
                        [0, 0, 1]
                    ])

Refl = lambda m,c:  np.array([
                        [(1 - m**2)/(m**2 + 1),        2*m/(m**2 + 1), 0],
                        [       2*m/(m**2 + 1), (m**2 - 1)/(m**2 + 1), 0],
                        [    -2*c*m/(m**2 + 1),        2*c/(m**2 + 1), 0]
                    ]) if m != float('inf') else np.array([
                                                     [  -1,  0, 0],
                                                     [   0,  1, 0],
                                                     [ 2*c,  0, 1]
                                                 ])