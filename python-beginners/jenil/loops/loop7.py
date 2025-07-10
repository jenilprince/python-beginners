start = -1
end = int(input("range: "))
sum = 0
while start<=end:
    start = start + 2
    sum = sum + start
    print(start)
print(f"sum: {sum}")