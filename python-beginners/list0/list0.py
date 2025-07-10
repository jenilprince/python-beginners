'''l0=[1,2,3,4,5,6]
print(list[::2])
l1=[8,2,4,6,1,3]
l1.sort()
print(l1[1])
l2=[1,2,3,4,5,6,7,8]
count = len(l2)/2
for i in l2:
    if l2.index(i)==count:
        print(l2[:int(count)])
        print(l2[int(count):])

l3=[1,2,3,4,3,2,1,2,4,5,1]
new=[]
new1=[]
for i in l3:
    if i not in new:
        new.append(i)
    else:
        new1.append(i)
st = set(new1)
print(list(st))'''







