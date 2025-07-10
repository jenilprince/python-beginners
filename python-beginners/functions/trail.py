def add():
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    sum=a+b
    print(sum)
def sub():
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    sum=a-b
    print(sum)
choice =int(input("enter 1 for additon 2 sub"))
if choice==1:
    add()
elif choice==2:
    sub()