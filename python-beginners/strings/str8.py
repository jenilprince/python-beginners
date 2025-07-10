try:
    def num():
        num=int(input("Enter a number: "))
    num()
except ValueError:
    print(f"INVALID")
else:
    print(f"VALID")