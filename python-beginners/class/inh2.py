class Person:
    def introduce(self):
        print("Person")
class Student(Person):
    def study(self):
        print("Student")
class CollegeStudent(Student):
    def attend_class(self):
        print("College Student")
std=CollegeStudent()
std.introduce()
std.study()
std.attend_class()

