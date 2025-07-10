#SPY NUMBER#
num = int(input("Enter a number: "))
sum = 0
prod =1
while num!=0:
    lastdig = num%10
    sum+=lastdig
    prod*=lastdig
    num=num//10
print(f"Product of digits = {prod}")
print(f"Sum of digits = {sum}")
if sum==prod:
    print("Spy Number")
else:
    print("Not Spy Number")