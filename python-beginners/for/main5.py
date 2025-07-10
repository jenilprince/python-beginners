n = int(input("Enter start number: "))
sum = 0
count = 0
for i in range(n, n+10):
    print(i)
    sum+=i
    count+=1
print(f"Sum = {sum}")
print(f"Count = {count}")
print(f"Average = {sum/count}")

