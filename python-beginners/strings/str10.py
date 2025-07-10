while True:
    try:
        num=int(input("Enter a number: "))
        break
    except ValueError:
        print("Invalid input")
print("Success")