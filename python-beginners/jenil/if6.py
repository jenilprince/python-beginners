side1 = float(input("Side1: "))
side2 = float(input("Side2: "))
side3 = float(input("Side3: "))
if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    print("Valid triangle")
else:
    print("Invalid triangle")
