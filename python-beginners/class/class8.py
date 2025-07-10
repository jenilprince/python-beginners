class Laptop:
    def __init__(self, brand, RAM, processor):
        self.brand=brand
        self.RAM=RAM
        self.processor=processor
    def start(self):
        print("Laptop is starting...")
    def display(self):
        print(self.brand, self.RAM, self.processor)
l1=Laptop("Brand1", "RAM1", "processor1")
l1.display()
l1.start()
l2=Laptop("Brand2", "RAM2", "processor2")
l2.display()