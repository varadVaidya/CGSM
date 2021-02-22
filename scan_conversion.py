#### CGSM Algorithms for the course MEL 432 Computer Graphics and Solid Modelling
#### Made by:
#### Varad Vaidya
#### BT18MEC060 

### DDA and Bresenham's line algorithm are implemented here:
import numpy as np
class DDA_ScanConversion():
    ## implementation of the DDA algorithm for making a line in betweeen a set of two points.
    '''
    all the points should be an numpy array..
    
    '''
    
    def __init__(self):
        pass
    
    @staticmethod
    def DDA_Line(point0,point1):
        """
        returns a list of points that will make a line between point 1 and point 2.
        args: point1 and point2 should be a numpy array..
        returns: list with all the points to be plotted..
        """
        
        dx,dy = point1 - point0
        linePoints = []
        
        step = abs(dx) if abs(dx) > abs(dy) else abs(dy)
        
        interPoint = point0
        
        Xinc = dx/step
        Yinc = dy/step
        
        for i in range (step +1):
            
            # interPoint = np.rint(interPoint)
            # linePoints.append(interPoint)
            # interPoint = interPoint + [Xinc,Yinc]
            
            roundedInterPoint = np.rint(interPoint)
            linePoints.append(roundedInterPoint)
            interPoint = interPoint + [Xinc,Yinc]
            
        print(linePoints)
        
        pass
        
        
if __name__ == "__main__":
    
    point0,point1 = np.array([-3,2]),np.array([6,4])
    DDA_ScanConversion.DDA_Line(point0,point1)
    