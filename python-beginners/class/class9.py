class Fan:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
        self.is_on = "ON"
    def is_on(self):
        self.is_on = "ON"
    def is_off(self):
        self.is_on = "OFF"
    def display(self):
        print(self.brand, self.speed, self.is_on)
f1=Fan("Brand1", 1)
f2=Fan("Brand2", 2)
f2.is_off()
f1.is_off()
f1.display()
f2.display()