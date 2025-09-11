from shape import Shape
class Circle(Shape):
    def __init__(self,r1):
        self.r1=r1
    def area(self):
        print("Area if circle is ",3.14*self.r1*self.r1)  
        
c1=Circle(5)          
c1.area()