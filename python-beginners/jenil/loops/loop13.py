start = 1
num = int(input("No. "))
upto = int(input("Upto where: "))
j=1
while num>=1:
    while j <= upto:
        multiply = start*num
        j=j+1
        print(f"{start}*{num} = {multiply}")
        start = start+1
        multiply = num*j


