#############################################
# @name = Aditya Shirwatkar
# @github = aditya-shirwatkar
# @copyright = None 
#############################################

import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np

def Bresenham_Circle(r):
    interPoints = np.array([0, r])
    linePoints = []
    p = ['nan']
    p_current = 1-r
    p.append(p_current)
    linePoints.append(interPoints.tolist())

    while interPoints[0] < interPoints[1]:
        if p_current < 0:
            p_current += 2*(interPoints[0]) + 1
            p.append(p_current)
            interPoints = interPoints + np.array([1, 0])
            linePoints.append(interPoints.tolist())
        else:
            p_current += 2*(interPoints[0]-interPoints[1]) + 1
            p.append(p_current)
            interPoints = interPoints + np.array([1, -1])
            linePoints.append(interPoints.tolist())

    return linePoints, p

r = 8
origin = np.array([0, 0])
linePoints, p = Bresenham_Circle(r)

circle = np.array(linePoints) # 1/8th Q1
circle_1 = np.vstack((circle, np.flip(np.flip(circle, axis=0), axis=1))) # 1/4th Q1

circle_4 = np.hstack((circle_1[:,0].reshape(-1,1), (circle_1[:,1]*-1).reshape(-1,1))) # 1/4th Q4

circle_14 = np.vstack((circle_1, circle_4)) # 1/2 - Q14
circle_23 = -circle_14 # 1/2 - Q23

circle = np.vstack((circle_14, circle_23))

import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np

N = len(circle)//2
# make an empty data set
data = np.ones((N, N)) * np.nan
scale_x = 0
scale_y = 0
# fill in some fake data
for point in circle.tolist():
    a = N - (N//2 + point[1] + scale_y)
    b = (point[0] + scale_x + N//2)
    # print(a, b)
    data[a, b] = 1

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

print('1/8th circle: ', linePoints)
print('p: ', p)
print('##########################')
print('Full circle with shifted origin')
print((circle + origin).tolist())
plt.show()