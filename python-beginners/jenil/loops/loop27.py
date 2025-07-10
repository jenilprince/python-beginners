## DISPLAY ARMSTRONG NUMBER -- eg. 153 = 1**3 + 5**3 + 3**3##
start = int(input("Enter start number: "))
end = int(input("Enter end number: "))
while start<=end:
    start1 = start
    count = 0
    while start1!=0:
        count+=1
        start1 = start1//10
    start2 = start
    sum = 0
    while start2!=0:
        last = start2%10
        sum = sum+last**count
        start2 = start2//10
    if sum==start:
        print(start)
    start+=1

