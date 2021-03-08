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
        print("dx,dy is:" ,dx,dy)
        linePoints = []
        
        step = abs(dx) if abs(dx) > abs(dy) else abs(dy)
        print("the step size is: ", step)
        interPoint = point0
        
        Xinc = dx/step
        Yinc = dy/step
        print("Xinc and Yinc is ", Xinc, Yinc)
        for i in range (step +1):
            
            # interPoint = np.rint(interPoint)
            # linePoints.append(interPoint)
            # interPoint = interPoint + [Xinc,Yinc]
            
            roundedInterPoint = np.rint(interPoint)
            linePoints.append(roundedInterPoint)
            interPoint = interPoint + [Xinc,Yinc]
            print(interPoint)
        
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
        returns: list with all the points and p values to be plotted..
        """
        
        dx,dy = point1 - point0
        dx=abs(dx)
        dy=abs(dy)
        linePoints = []
        p = []
        p.append(2*dx - dy)
        p_current=2*dx-dy
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
                if p_current > 0 :
                    interPoint = interPoint+[1,1]
                    linePoints.append(interPoint)
                    p.append(p_current+(twody-twodx))
                    p_current = p_current+(twody-twodx)
                else:
                    interPoint = interPoint+[1,0]
                    linePoints.append(interPoint)
                    p.append(p_current+twody)
                    p_current = p_current+twody
                dx-=1
                i+=1 
        ## for m >1
        else:
            if point0[0]>point1[0]:
                interPoint = point1
            else:
                interPoint = point0
            linePoints.append(interPoint)
            while dy>0 :
                if p_current > 0:
                    interPoint = interPoint+[1,1]
                    linePoints.append(interPoint)
                    p.append(p_current+(twodx-twody))
                    p_current = p_current+(twodx-twody)
                    
                else:
                    interPoint = interPoint+[0,1]
                    linePoints.append(interPoint)
                    p.append(p_current+twodx)
                    p_current = p_current+twodx
                    
                dy-=1
                i+=1
        return linePoints,p 
        #print(linePoints)
    
    
    @staticmethod
    def Bresenham_Circle(Origin,r):
        interPoints = np.array([0,r])
        linePoints = []
        p = []
        p.append(1-r)
        p_current=1-r
        linePoints.append(interPoints)
        print(interPoints)
        while interPoints[0]<interPoints[1]:
            if p_current<0:
                p_current=p_current+ 2*(interPoints[0])+1
                p.append(p_current)
                interPoints = interPoints + np.array([1,0])
                linePoints.append(interPoints)
            else:
                p_current=p_current+ 2*(interPoints[0]-interPoints[1]) + 1
                p.append(p_current)
                interPoints = interPoints + np.array([1,-1])
                linePoints.append(interPoints)
        return linePoints,p 
        #print(linePoints)

            



if __name__ == "__main__":
    
    pointList = [ np.array([-1,-2]),np.array([5, 0])]     
    # polyList,p = Bresenham_ScanConversion.Bresenham_Circle(Origin=np.array([-1,-2]),r=5)
    polyList,p = Bresenham_ScanConversion.Bresenham_Line(pointList[0], pointList[1])
    
    # print(polyList) # 1/4th points
    # print(p)
    
    pointList = [np.array([0,0]),np.array([6,7])]
    
    lineDDA = DDA_ScanConversion.DDA_Line(point0=pointList[0],point1=pointList[1])
    print(lineDDA)
    
    
    

    