class Shape:
    def __init__(self):
        pass
class Rectangle(Shape):
    def __init__(self, width, height):
        Shape.__init__(self)
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
class Circle(Shape):
    def __init__(self, radius):
        Shape.__init__(self)
        self.radius = radius
        
    def area(self):
        return 3.14 * self.radius * self.radius
l=[]
l.append(Rectangle(4,5))
l.append(Circle(3))
for sameshape in l:
    print (sameshape.area())