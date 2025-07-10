start = int(input("Enter start number: "))
end = int(input("Enter end number: "))
while start<=end:
    temp = start
    sum= 0
    while temp!=0:
        last = temp%10
        sum += last
        temp = temp//10
    if start%sum==0:
        print(start)
    start+=1

