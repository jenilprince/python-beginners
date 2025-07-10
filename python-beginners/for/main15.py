## Check spy number - sum of dig = prod of dig ##
num = 1124
sum = 0
prod = 1
b = str(num)
for i in b:
    sum += int(i)
    prod *= int(i)
print(f"Sum of digits = {sum}")
print(f"Product of digits = {prod}")
if sum == prod:
    print(f"Spy number")
else:
    print(f"NOT Spy number")
