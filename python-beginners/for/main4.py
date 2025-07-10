"""
list0 = ["Apple", "Orange", "Banana", "Pineapple", "Strawberry"]
print(list0)
list1 = [1,2,3,4,5]
print(list1[2])

list2 = ["Red", "Green", "Blue", "Purple", "Yellow", "Orange", "White", "Black"]
print(list2[:-3])

list3= ["Lion", "Tiger", "Giraffe"]
list3.append("Cow")
print(list3)

list4=[1,3,4,5]
list4.insert(1,2)
print(list4)

list5=[1,2,3,4,5]
list5.remove(4)
print(list5)

list6 = [1,2,3,4,5]
popd = list6.pop(4)
print(popd)

l7= ["Apple", "Orange", "Banana", "Pineapple", "Strawberry"]
print(l7.index("Banana"))
print(l7.index("Strawberry"))

l8=[1,2,2,2,3,3,4,5,6,7,8,9,9,3,3,2,4,5,6,11,1,1,1,1,66,75,9,0]
print(l8.count(3))

l9=[9,7,5,3,1,2,4,6,8,0]
l9.sort(reverse=False)
print(l9)

l10=["Apple", "Orange", "Banana", "Pineapple", "Strawberry"]
l10.sort(reverse=True)
print(l10)
l11=[1,2,3,5,6,7777,6,543,30,0]
print(len(l11))

l00=[1,2,3]
l01=["A", "B", "C"]
print(l00+l01)

l99=["Cat", "Dog", "Sheep"]
if "Cat" in l99:
    print("True")
else:
    print("False")

l98=[1,2,3,4,5,6]
for i in l98:
    print(i, end=" ")

l23=[[1,2,3],[4,5,6]]
print(l23[0][1])

a=[1,2,4]
c=a.copy()
a.append(8)
print(a)
print(c)
"""
a=[x for x in range(1,100)]



print(a)