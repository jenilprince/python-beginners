## TO CHECK PALINDROME NUMBER eg. 121, 1331, 1221, 22, 44, 4554, 12321##
num = 2
reversed = 0
num1 = num
#123 = 100*1 + 10*2 + 1*3#
while num1!=0:
    last = num1%10
    reversed=reversed*10+last
    num1 = num1//10
print(reversed)
if reversed == num:
    print("Palindrome")
else:
    print("Not Palindrome")












