## CHECK HARSHAD NUMBER - no. divisible by sum of digits ##
num = 11
sum = 0
num1 = num
for i in range(num):
    last = num%10
    sum = sum + last
    num = num//10
print(f"Sum == {sum}")
if num1%sum == 0:
    print("Harshad Number")
elif num1%sum != 0:
    print("NOT Harshad Number")