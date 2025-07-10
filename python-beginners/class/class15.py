class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius
    def fah(self):
        fah = (self.celsius * 1.8) + 32
        print(fah)
    def display(self):
        print(self.celsius)
t1=Temperature(37)
t1.display()
t1.fah()