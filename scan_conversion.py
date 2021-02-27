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
        
        return linePoints 
        #print(linePoints)
        
        
    @staticmethod
    def DDA_Polygon(pointList):
        
        polygonPointList = []
        numPoints = len(pointList)
        
        print("Your polygon is a triange") if len(pointList) == 3 else print("its not a triangle")
        
        for i in range(numPoints):
            
            linePoints = DDA_ScanConversion.DDA_Line(pointList[i-1],pointList[i])
            
            polygonPointList.append(linePoints)
            
        return polygonPointList           
        
class Bresenham_ScanConversion():
    ## implementation of the Bresenham algorithm for making a line in betweeen a set of two points.
    '''
    all the points should be an numpy array..
    
    '''
    
    def __init__(self):
        pass
    
    @staticmethod
    def Bresenham_Line(point0,point1):
        """
        returns a list of points that will make a line between point 1 and point 2.
        args: point1 and point2 should be a numpy array..
        returns: list with all the points to be plotted..
        """
        
        dx,dy = abs(point1 - point0)
        linePoints = []
        p = []
        p.append(2*dy-dx)
        twody=2*dy 
        twodx=2*dx
        i=0
        ## For m<1
        if abs(dx) > abs(dy):
            if point0[0]>point1[0]:
                interPoint = point1
            else:
                interPoint = point0
            linePoints.append(interPoint)
            while dx>0 :
                if p[i]>0:
                    linePoints.append(interPoint[0]+1,interPoint[1]+1)
                    p.append(p+(twody-twodx))
                else:
                    linePoints.append(interPoint[0]+1,interPoint[1]+1)
                    p.append(p+twody)
                dx-=1
                i+=1 
        ## for m >1
        if abs(dy) > abs(dx):
            if point0[1]>point1[1]:
                interPoint = point1
            else:
                interPoint = point0
            linePoints.append(interPoint)
            while dy>0 :
                if p[i]>0:
                    linePoints.append(interPoint[0]+1,interPoint[1]+1)
                    p.append(p+(twodx-twody))
                else:
                    linePoints.append(interPoint[0],interPoint[1]+1)
                    p.append(p+twodx)
                dy-=1
                i+=1
        return linePoints,p 
        #print(linePoints)
if __name__ == "__main__":
    
    pointList = [ np.array([0,0]),np.array([4,6]),np.array([-3,2])]     
    polyList = DDA_ScanConversion.DDA_Polygon(pointList)
    print(polyList)
    

    