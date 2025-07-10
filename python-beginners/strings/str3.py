try:
    a=int(input("Enter 1st Number: "))
    b=int(input("Enter 2nd Number: "))
    print(a/b)
except ZeroDivisionError:
    print("ZeroDivisionError")
except ValueError:
    print("Enter a value")
else:
    print("No Error")
finally:
    print("Value")