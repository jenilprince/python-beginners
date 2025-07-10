## DISPLAY HARSHAD NOS. IN INTERVAL - NUMBER DIVISIBLE BY SUM OF DIGITS##
start = int(input("Start number: "))
end = int(input("End number: "))
for i in range(start, end+1):
    string= str(i)
    sum=0
    for j in string:
        temp = j
        last=int(temp)%10
        sum = sum + last
    if i%sum==0:
        print(i)

