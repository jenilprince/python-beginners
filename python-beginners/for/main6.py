## SUM OF A.P ##
sum = 0
a = int(input("First number of A.P: "))
d = int(input("Common difference of A.P: "))
n = int(input("Number of terms: "))
l = a + (n-1)*d
for i in range(a, l):
    sum = n/2*(a+l)
print(f"Sum == {sum}")