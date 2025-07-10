class x:
    def show(self):
        print("Hello")
class y:
    def show(self):
        super().show()
        print("Hai")
class z(y,x):
    def show(self):
        super().show()
        print("Hey")
r=z()
r.show()