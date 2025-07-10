start = 0
end = int(input("Range: "))
sum = 0
while start <= end:
    sum = sum + start
    start = start + 2
    print(start)
print(f"Sum: {sum}")