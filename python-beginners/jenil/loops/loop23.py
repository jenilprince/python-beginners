#DISPLAY PRIME NO.S IN INTERVAL#
start=int(input("enter a number "))
end=int(input("end number "))
while start<=end:
    num = start
    if num<1:
        print("Invalid number")
    else:
        factor = 2
        flag=0
        while factor<=num//2:
            if num%factor==0:
                flag=1
                break
            factor+=1
        if flag==0:
            print(num)
    start+=1
