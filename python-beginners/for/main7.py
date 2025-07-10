## DISPLAY SQUARE OF N NO.S AND SUM##
n = int(input("Enter a number: "))
sum = 0
for i in range (1, n+1):
    i = i**2
    sum+=i
    print(i)
print(f"Sum = {sum}")