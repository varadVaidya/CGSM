#############################################
# @name = Aditya Shirwatkar
# @github = aditya-shirwatkar
# @copyright = None 
#############################################

x1 = 0; x2 = 6
y1 = 0; y2 = 7

dx = (x2-x1)
dy = (y2-y1)

step = abs(dx) if abs(dx) > abs(dy) else abs(dy)

xpp = round(dx/step, 3); ypp = round(dy/step, 3)

x,y = x1,y1

points = [[x,y]]

print('######### INFO #########')
print('x1 = ', x1, ' ', 'y1 = ', y1)
print('x2 = ', x2, ' ', 'y2 = ', y2)
print('dx = ', dx, ' ', 'dy = ', dy, ' ', 'm = ', round(dy/dx, 3))
print('step = ', step)
print('xpp = ', xpp, ' ', 'ypp = ', ypp)

for i in range(step):
    x += xpp
    y += ypp

    points.append([int(x),int(y)])

print('Line', points)

import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np

N = 4*step
# make an empty data set
data = np.ones((N, N)) * np.nan
# fill in some fake data
for point in points:
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