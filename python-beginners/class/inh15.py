class X:
    def show(self):
        print('1')
class Y:
    def show(self):
        print('2')
class Z(X, Y):
    def show(self):
        super().show()
        print('3')
d=Z()
d.show()
