class MobilePhone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    def display(self):
        print(self.brand, self.model, self.price)
m1=MobilePhone("Vivo", "V23e", 25000)
m2=MobilePhone("Samsung", "S24", 100000)
m1.display()
m2.display()