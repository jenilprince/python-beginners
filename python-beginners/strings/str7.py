try:
    check_age=int(input("Enter age: "))
    if check_age<0:
        raise ValueError()
except ValueError:
    print("Invalid age")
else:
    print("Valid age")
