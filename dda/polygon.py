#############################################
# @name = Aditya Shirwatkar
# @github = aditya-shirwatkar
# @copyright = None 
#############################################

poly_locs = [[0,0], [0,5], [5,5], [7, 3], [5, -3]]

N0 = len(poly_locs)

poly_points = []

for i in range(N0): 
    x1 = poly_locs[i%N0][0]; x2 = poly_locs[(i+1)%N0][0]
    y1 = poly_locs[i%N0][1]; y2 = poly_locs[(i+1)%N0][1]

    dx = (x2-x1)
    dy = (y2-y1)

    step = abs(dx) if abs(dx) > abs(dy) else abs(dy)

    xpp = round(dx/step, 3); ypp = round(dy/step, 3)

    x,y = x1,y1

    points = [[x,y]]

    print('######### INFO #########')
    print('x1 = ', x1, ' ', 'y1 = ', y1)
    print('dx = ', dx, ' ', 'dy = ', dy, ' ', 'm = ', round(dy/dx, 3) if dx != 0 else 0)
    print('step = ', step)
    print('xpp = ', xpp, ' ', 'ypp = ', ypp)

    while (int(x) != x2) or (int(y) != y2):
        x += xpp
        y += ypp

        points.append([int(x),int(y)])

    print(points)

    poly_points += points
    points = []

import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np

N = 4*step
# make an empty data set
data = np.ones((N, N)) * np.nan
# fill in some fake data
for point in poly_points:
    data[N-1 - (N//2 + point[1]), (point[0] + N//2)] = 1

# make a figure + axes
fig, ax = plt.subplots(1, 1, tight_layout=True)
# make color map
my_cmap = colors.ListedColormap(['r', 'g', 'b'])
# set the 'bad' values (nan) to be white and transparent
my_cmap.set_bad(color='w', alpha=0)
# draw the grid
for x in range(N + 1):
    ax.axhline(x, lw=2, color='k', zorder=5)
    ax.axvline(x, lw=2, color='k', zorder=5)
# draw the boxes
ax.imshow(data, interpolation='none', cmap=my_cmap, extent=[0, N, 0, N], zorder=0)
# turn off the axis labels
ax.axis('off')

plt.show()