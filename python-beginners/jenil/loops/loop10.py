start = 1
end = int(input("Range: "))
sum = 0
while start<=end:

    square = start**2
    start = start +1
    sum = sum + square
    print(square)
print(sum)


