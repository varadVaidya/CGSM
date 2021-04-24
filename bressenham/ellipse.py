#############################################
# @name = Aditya Shirwatkar
# @github = aditya-shirwatkar
# @copyright = None 
#############################################

import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np

def Bresehem_Ellipse(a,b): # a is major and b is minor
    # Region 1
    interPoints = np.array([0, b])
    linePoints = []
    p1 = ['nan']
    p1_current = b**2 - (a**2)*b + 0.25*(a**2)
    p1.append(p1_current)
    linePoints.append(interPoints.tolist())

    while (b**2)*interPoints[0] < (a**2)*interPoints[1]:
        if p1_current < 0:
            interPoints = interPoints + np.array([1, 0])
            linePoints.append(interPoints.tolist())
            if (b**2)*interPoints[0] < (a**2)*interPoints[1]:
                p1_current += 2*(b**2)*(interPoints[0]) + b**2
                p1.append(p1_current)
        else:
            interPoints = interPoints + np.array([1, -1])
            linePoints.append(interPoints.tolist())
            if (b**2)*interPoints[0] < (a**2)*interPoints[1]:
                p1_current += 2*(b**2)*(interPoints[0])-2*(a**2)*(interPoints[1]) + b**2
                p1.append(p1_current)
    
    # Region 2
    p2 = []
    p2_current = (b**2)*(interPoints[0] + 0.5)**2 + (a**2)*(interPoints[1]-1) - (a*b)**2
    p2.append(p2_current)

    while  interPoints[1] > 0:
        if p2_current >= 0:
            interPoints = interPoints + np.array([0, -1])
            linePoints.append(interPoints.tolist())
            if interPoints[1] > 0:
                p2_current += -2*(a**2)*(interPoints[1]) + a**2
                p2.append(p2_current)
        else:
            interPoints = interPoints + np.array([1, -1])
            linePoints.append(interPoints.tolist())
            if interPoints[1] > 0:
                p2_current += 2*(b**2)*(interPoints[0])-2*(a**2)*(interPoints[1]) + a**2
                p2.append(p2_current)
    
    return linePoints, p1, p2

a,b = (6,2) # a is major/2 and b is minor/2
origin = np.array([-5, 2])
linePoints, p1, p2 = Bresehem_Ellipse(a,b)

ellipse_1 = np.array(linePoints) # 1/4th Q1

ellipse_4 = np.hstack((ellipse_1[:,0].reshape(-1,1), (ellipse_1[:,1]*-1).reshape(-1,1))) # 1/4th Q4

ellipse_14 = np.vstack((ellipse_1, ellipse_4)) # 1/2 - Q14
ellipse_23 = -ellipse_14 # 1/2 - Q23

ellipse = np.vstack((ellipse_14, ellipse_23))

import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np

N = len(ellipse)//2
# make an empty data set
data = np.ones((N, N)) * np.nan
scale_x = 0
scale_y = 0
# fill in some fake data
for point in ellipse.tolist():
    a = N - (N//2 + (point[1]) + scale_y)
    b = ((point[0]) + scale_x + N//2)
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

print('1/4th ellipse: ', linePoints)
print('p1: ', p1)
print('p2: ', p2)
print('1/4th ellipse shifted: ', (ellipse_1+origin).tolist())
print('##########################')
print('Full ellipse with shifted origin')
print((ellipse + origin).tolist())
plt.show()