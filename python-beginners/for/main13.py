## FIBONACCI SEQUENCE 1st 'n' terms ##
n = int(input("Enter a number: "))
fib1 = 0
fib2 = 1
for i in range(0,n+1):
    print(fib1)
    fib3 = fib1 + fib2
    fib1 = fib2
    fib2 = fib3
