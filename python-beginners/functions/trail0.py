## CALCULATOR ##
def add():
    a=int(input("Enter 1st number: "))
    b=int(input("Enter 2nd number: "))
    add=a+b
    print(f"Sum == {add}")
def sub():
    a=int(input("Enter 1st number: "))
    b=int(input("Enter 2nd number: "))
    sub=a-b
    print(f"Difference == {sub}")
def mul():
    a=int(input("Enter 1st number: "))
    b=int(input("Enter 2nd number: "))
    mul=a*b
    print(f"Product == {mul}")
def div():
    a=int(input("Enter 1st number: "))
    b=int(input("Enter 2nd number: "))
    div=a/b
    print(f"Quotient == {div}")
def floordiv():
    a=int(input("Enter 1st number: "))
    b=int(input("Enter 2nd number: "))
    floordiv=a//b
    print(f"Quotient without decimal == {floordiv}")
def mod():
    a=int(input("Enter 1st number: "))
    b = int(input("Enter 2nd number: "))
    mod=a%b
    print(f"Remainder after division == {mod}")
def exp():
    a=int(input("Enter 1st number: "))
    b=int(input("Enter power: "))
    exp=a**b
    print(f"{a} to the power {b} == {exp}")
def avg():
    a=int(input("Enter 1st number: "))
    b=int(input("Enter 2nd number: "))
    avg=(a+b)/2
    print(f"Average == {avg}")
choice=input('''
**INSTRUCTIONS**

A for Addition
S for Subtraction
M for Multiplication
D for Division
F for FloorDivision
R for Remainder
E for Exponentiation
Av for Average

Enter your choice: ''')
if choice.lower()=='a':
    add()
elif choice.lower()=='s':
    sub()
elif choice.lower()=='m':
    mul()
elif choice.lower()=='d':
    div()
elif choice.lower()=='f':
    floordiv()
elif choice.lower()=='r':
    mod()
elif choice.lower()=='e':
    exp()
elif choice.lower()=='av':
    avg()