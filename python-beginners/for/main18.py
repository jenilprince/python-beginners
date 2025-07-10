##check prime or not
n = int(input("Enter a number: "))
for i in (2,n):
    flag=0
    if n%i!=0:
        print("PRIME")
        break
    else:
        print("Not prime")


