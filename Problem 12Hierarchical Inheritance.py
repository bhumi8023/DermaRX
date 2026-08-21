class Shape:
    def __init__(self,edge):
        self.edge = edge
        print("All shape have differnt edges")

class Rectangle(Shape):
    def __init__(self, edge):
        super().__init__(edge)
        print("Area of rectangle is l*b")

class Circle(Shape):
    def __init__(self, edge):
        super().__init__(edge)
        print("perimeter of circle is 2*3.14*r")

c1 = Circle(0)
r1 = Rectangle(4)
        