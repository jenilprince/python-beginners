#ARMSTRONG NUMBER#
#Eg. 153 = 1**3 + 5**3 + 3**3 #

num=int(input("Enter a number: "))
t=num
count = 0
while t>0:
    lastdig = t%10
    count +=1
    t=t//10
print(f"Count = {count}")

sum = 0
while num>0:
    lastdig = num%10
    sum = sum + lastdig**count
    num = num//10
print(f'Sum = {sum}')
if num == sum:
    print("Armstrong number")
else:
    print("Not Armstrong number")





