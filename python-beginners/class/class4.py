class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        area = self.length*self.width
        print(area)
a1=Rectangle(10,20)
a2=Rectangle(10,8)
a1.area()
a2.area()