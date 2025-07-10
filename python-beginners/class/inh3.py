class Shape:
    def draw(self):
        print('draw')
class Rectangle(Shape):
    def calculate_area(self):
        print('calculate area')
class ColoredRectangle(Rectangle):
    def fill_color(self):
        print('fill color')
r=ColoredRectangle()
r.fill_color()
r.calculate_area()
r.draw()