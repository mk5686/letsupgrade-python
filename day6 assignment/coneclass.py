import math
class cone: 
    def __init__(self, height,radius): 
        self.height=float(height)
        self.radius=float(radius)
        
        
        
    def getdetails(self):
        print("height",self.height)
        print("radius",self.radius)

    def volume(self): 
        v=(1/3)*(math.pi*self.radius**2*(self.height))
        print("volume of the cone is\n",v)

    def area(self):
    	side=math.pi*self.radius*math.sqrt(self.radius**2+self.height**2)
    	a=math.pi* self.radius * side + math.pi*self.radius**2
    	print("area of cone is \n",a)



c=cone(5,4)
c.getdetails()
c.volume()
c.area()

