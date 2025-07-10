#CHECK PRIME NUMBER#
num = int(input("Enter a number: "))
div = 1
if num<1:
    print("Invalid input")
count = 0
while div<=num:
    if num%div == 0:
        print (div)
        count+=1
    div+=1
print(f"Count: {count}")
if count == 2:
    print("Prime number")
else:
    print("Not prime")
