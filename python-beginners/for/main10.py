## TO DISPLAY MULTIPLICATION TABLE FRM 1 TO n##
n = int(input("Enter a number: "))
c = 0
for i in range(1, n+1):
    for c in range(1, 11):
        print(f"{i} * {c} = {i * c}")
        c+=1
    i+=1
