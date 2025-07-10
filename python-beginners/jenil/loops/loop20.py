#TO FIND FACTORS OF A NUMBER#
num = int(input("Enter a number: "))
start=1
while start<=num:
    if num%start==0:
        print(start)
    start=start+1
