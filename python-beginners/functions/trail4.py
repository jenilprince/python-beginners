#MULTIPLICATION TABLE#
def table(a):
    temp = a
    if temp<0:
        print("The number cannot be negative.")
    else:
        for i in range(1,11):
            print(f"{i} * {a} = {a*i}")
            i+=1
table(12)