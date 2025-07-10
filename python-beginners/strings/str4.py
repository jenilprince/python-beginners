try:
    a=int(input("Enter a number: "))
    print(100//a)
except (ZeroDivisionError, ValueError) as e:
    print("zeor njot")


