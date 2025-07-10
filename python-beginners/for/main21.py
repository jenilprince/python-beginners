##DISPLAY ARMSTRONG NO.S IN INTERVAL##
start = int(input("Start number: "))
end = int(input("End number: "))
for i in range (start, end+1):
    b=str(i)
    pow=0
    for j in b:
        pow=pow+1
    sum=0
    for j in b:
        last = int(j)%10
        sum = sum + last**pow
    if sum==i:
        print(i)


