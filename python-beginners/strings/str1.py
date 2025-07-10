'''p="Python for Beginners"
rever=" "
for i in p:
    rever=i+rever
print(rever)
print(p[::-1])
print(p.split())
list_of_words=['Python', 'for', 'Beginners']
print(' '.join(list_of_words))
char="Python, for, Beginners.!?"
remove=",.?!"
no=""
for i in char:
    if i not in remove:
        no=no+i
print(no)'''
p1="Python for Beginners"
print(p1.index("for"))
space=" "
count=1
for i in p1:
    if i in space:
        count=count+1
print(f"Count = {count}")




