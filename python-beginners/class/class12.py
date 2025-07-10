class Employee:
    def __init__ (self):
        self.name = input("Enter your name: ")
        self.id=int(input("Enter your id: "))
        self.salary=int(input("Enter your salary: "))
    def display(self):
        print("Name:",self.name)
        print("id:",self.id)
        print("Salary:",self.salary)
e1=Employee()
e1.display()