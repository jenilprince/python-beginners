try:
    a=10
    b=int(input("enter a number:"))
    print(a/b)
except ZeroDivisionError:
    print("ZeroDivisionError")
except ValueError:
    print("ValueError")
else:
    print("success")
finally:
    print("i run every time")