start = 100
sum = 0
av = 0
count = 0
while start <= 200:
    if start%9==0:
        sum = sum +start
        count = count + 1
    start = start + 1
av = sum/count
print(sum)
print(av)



