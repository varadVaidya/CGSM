#############################################
# @name = Aditya Shirwatkar
# @github = aditya-shirwatkar
# @copyright = None 
#############################################

# x1, y1 should be lower

x1 = -1; x2 = 1
y1 = -2; y2 = 4

m = round((y2-y1)/(x2-x1), 3) if (x2-x1) != 0 else 100000000 # used just to represnt inf

dx = abs(x2-x1)
dy = abs(y2-y1)
two_dy = 2*dy 
two_dx = 2*dx

linePoints = []
p = []
p_current = 2*dy - dx
p.append(p_current)

i=0

print('######### INFO #########')
print('x1 = ', x1, ' ', 'y1 = ', y1)
print('x2 = ', x2, ' ', 'y2 = ', y2)
print('dx = ', dx, ' ', 'dy = ', dy, ' ', 'm = ', m)

## For m<1
if m < 1:
    if abs(dx) > abs(dy):
        if x1 > x2:
            x, y = x2, y2
        else:
            x, y = x1, y1
        
        linePoints.append([x, y])

        while dx>0 :
            if p_current > 0 :
                x, y = x+1, y+1
                linePoints.append([x, y])
                p_current += (two_dy - two_dx)
                p.append(p_current)
            else:
                x += 1
                linePoints.append([x, y])
                p_current += two_dy
                p.append(p_current)
            
            dx-=1
            i+=1
## for m >1
else:
    if y1>y2:
        x,y = x2, y2
    else:
        x,y = x1, y1
    
    linePoints.append([x, y])
    
    while dy>0 :
        if p_current > 0:
            x, y = x+1, y+1
            linePoints.append([x, y])
            p_current += two_dx - two_dy
            p.append(p_current)            
        # elif p_current > 0 and dx == 0:
        #     y += 1
        #     linePoints.append([x, y])
        #     p_current += two_dx - two_dy
        #     p.append(p_current)
        else:
            y += 1
            linePoints.append([x, y])
            p_current += two_dx
            p.append(p_current)
    
        dy-=1
        i+=1

print('Line', linePoints)
print('-----------')
print('p', p)


import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np

N = 4*len(linePoints)
# make an empty data set
data = np.ones((N, N)) * np.nan
# fill in some fake data
for point in linePoints:
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