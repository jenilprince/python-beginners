start =  int(input("from: "))-1
end = start+9
sum = 0
avg = 0
while start<=end:
    start = start + 1
    sum = sum + start
    avg = sum/start
    print(start)
print(sum)
print(avg)