#############################################
# @name = Aditya Shirwatkar
# @github = aditya-shirwatkar
# @copyright = None 
#############################################

# y1 should be lower

x1 = 0; x2 = -4
y1 = 2; y2 = 7

m = round((y2-y1)/(x2-x1), 3) if (x2-x1) != 0 else 100000000 # used just to represnt inf

dx = abs(x2-x1)
dy = abs(y2-y1)
two_dy = 2*dy 
two_dx = 2*dx

linePoints = []
p = ['nan']
x,y = x1,y1
linePoints.append([x,y])
    
print('######### INFO #########')
print('x1 = ', x1, ' ', 'y1 = ', y1)
print('x2 = ', x2, ' ', 'y2 = ', y2)
print('dx = ', dx, ' ', 'dy = ', dy, ' ', 'm = ', m)

if 0 <= m <= 1:
    p_current = 2*dy - dx
    p.append(p_current)
    while x<x2 :
        if p_current >= 0 :
            x, y = x+1, y+1
            linePoints.append([x, y])
            p_current += (two_dy - two_dx)
            p.append(p_current)
        else:
            x += 1
            linePoints.append([x, y])
            p_current += two_dy
            p.append(p_current)

elif m > 1:
    p_current = 2*dx - dy
    p.append(p_current)
    while y<y2 :
        if p_current >= 0 :
            x, y = x+1, y+1
            linePoints.append([x, y])
            if y<y2:
                p_current += (two_dx - two_dy)
                p.append(p_current)
        else:
            y += 1
            linePoints.append([x, y])
            if y<y2:
                p_current += two_dx
                p.append(p_current)

if -1 <= m <= -0:
    p_current = 2*dy - dx
    p.append(p_current)
    while x>x2 :
        if p_current >= 0 :
            x, y = x-1, y+1
            linePoints.append([x, y])
            p_current += (two_dy - two_dx)
            p.append(p_current)
        else:
            x -= 1
            linePoints.append([x, y])
            p_current += two_dy
            p.append(p_current)
elif m < -1:
    p_current = 2*dx - dy
    p.append(p_current)
    while y<y2 :
        if p_current >= 0 :
            x, y = x-1, y+1
            linePoints.append([x, y])
            if y<y2:
                p_current += (two_dx - two_dy)
                p.append(p_current)
        else:
            y += 1
            linePoints.append([x, y])
            if y<y2:
                p_current += two_dx
                p.append(p_current)
        

print('Line', linePoints)
print('-----------')
print('p', p)


import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np

N = 4*len(linePoints)
# make an empty data set
data = np.ones((N, N)) * np.nan
scale_x = - abs(x2)
scale_y = - abs(y2)
# fill in some fake data
for point in linePoints:
    a = N - (N//2 + point[1] + scale_y)
    b = (point[0] + scale_x + N//2)
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

plt.show()