## DISPLAY PRIMES IN INTERVAL ##
start = int(input ("Enter start number: "))
end = int(input ("Enter end number: "))
for i in range(start,end+1):
    if i<1:
        print("Not possible")
    else:
        flag = 0
        for j in range(2,i//2):
            if i%j==0:
                flag = 1
                break
        if flag==0:
            print(i)
