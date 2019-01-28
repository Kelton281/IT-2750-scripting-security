import math
def archimedes(numsides, radius): 
        innerangleB = 360.0/numsides 
        halfangleA = innerangleB/2 
        onehalfsideS  = math.sin(math.radians(halfangleA)) * radius
        sideS = onehalfsideS * 2 
        polygonCircumference = numsides * sideS 
        pi = polygonCircumference/(2 * radius) 
        return pi

        

        
        
        

   