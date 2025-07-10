class Person:
    def greet(self):
        print('Hello')
class Student(Person):
    def greet(self):
        super().greet()
        print('Hello student')
c=Student()
c.greet()
