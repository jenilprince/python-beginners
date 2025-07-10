sum=0
num=int(input("Enter a number: "))
temp=num
while num!=0:
    last =num%10
    sum=sum+last
    num=num//10
if (temp%sum==0):
    print("Harshad number")
else:
    print("Not Harshad number")