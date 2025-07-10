a = int(input('First number of A.P: '))
d = int(input('Diff of A.P: '))
n = int(input('Number of terms of A.P: '))
an = a+(n-1)*d
start = 0
sum = 0
while start < n:
    start = start + d
    sum = n/2*(a+an)
print(sum)



