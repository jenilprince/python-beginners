class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def minor(self,age):
        if age < 18:
            print("minor")
        else:
            print("adult")
    def display(self):
        print(self.name, self.age)
s1=Person("Name1", 20)
s2=Person("Name2", 12)
s1.display()
s1.minor(20)
s2.display()
s2.minor(12)
