##CHECK ARMSTRONG NUMBER eg. 153 ##
num= int(input("Enter a number: "))
sum = 0
pow = 0
st = str(num)
for i in st:
    pow+=1
print(pow)
for i in st:
    sum=sum+int(i)**pow
print(sum)
if sum == num:
    print("YES")
else:
    print("NO")
