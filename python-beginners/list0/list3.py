a=[6,5,4,3,2,1,7,8,9,10]
sum=0
temp = a
for i in temp:
    sum+=i
print(sum)
av=sum/len(a)
print(av)
a.sort()
temp1=a
new=[]
for j in temp1:
    if j>=av:
        new.append(j)
print(new)


