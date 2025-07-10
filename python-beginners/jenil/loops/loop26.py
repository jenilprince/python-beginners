## DISPLAY SPY NUMBERS -- sum of dig = prod of dig##
start = int(input("Enter the start number: "))
end=int(input("Enter the end number: "))
while start<=end:
    start1 = start
    sum = 0
    prod = 1
    while start1!=0:
        last = start1%10
        sum+=last
        prod*=last
        start1 = start1//10
    if sum == prod:
        print(start)
    start+=1





