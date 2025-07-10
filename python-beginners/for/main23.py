## DISPLAY SPY NUMBER IN INTERVAL - sum of dig = prod f dig ##
start = int(input("Start number: "))
end = int(input("End number: "))
for i in range(start, end+1):
    string = str(i)
    sum = 0
    prod=1
    for j in string:
        last = int(j)%10
        sum+=last
        prod*=last
    if sum==prod:
        print(i)
