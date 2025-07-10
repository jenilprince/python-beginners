class Dog:
    def __init__(self, name, breed, age):
        self.name=name
        self.breed=breed
        self.age=age
    def  bark(self):
        print("Woof!")
    def display(self):
        print(self.name, self.breed, self.age)
d1=Dog("name1", "breed1", 1)
d1.display()
d1.bark()
d2=Dog("name2", "breed2", 2)
d2.display()
d2.bark()