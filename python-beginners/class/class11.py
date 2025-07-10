class Student:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.rollNumber = input("Enter your roll number: ")
        self.marks = input("Enter your marks: ")
    def display(self):
        print(self.name, self.rollNumber, self.marks)
s1=Student()
s1.display()


