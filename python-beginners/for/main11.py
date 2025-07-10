## To find nos. bw 100 & 200 divisible by 9 and find SUM, AVG. ##
sum = 0
start = 100
end = 200
count = 0
for i in range(start, end+1):
    if i%9==0:
        print(i)
        sum += i
        count+=1
print(f"Count == {count}")
print(f"Sum == {sum}")
print(f"Average == {sum/count}")
