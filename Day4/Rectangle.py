from shape import Shape
class Rectangle(Shape):
    def __init__(self,l1,b1):
        self.l1=l1
        self.b1=b1
    def area(self):
        print("Area of rectangle is ",self.l1*self.b1)
        
rec1=Rectangle(10,20)
rec1.area()