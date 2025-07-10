class Animal:
    def breathe(self):
        print("Breathe")
class Mammal(Animal):
    def has_hair(self):
        print("Hair")
class Dog(Mammal):
    def bark(self):
        print("Bark")
d=Dog()
d.bark()
d.breathe()
d.has_hair()