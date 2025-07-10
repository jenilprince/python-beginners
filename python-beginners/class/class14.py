class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        area = 3.14*self.radius**2
        print(f"Area of the circle is {area}")
    def circumference(self):
        circumference = 2*3.14*self.radius
        print(f"Circumference of the circle is {circumference}")
    def display(self):
        print(f"Radius == {self.radius}")
c1=Circle(1)
c1.display()
c1.circumference()
c1.area()