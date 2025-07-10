with open('squares.txt', 'w') as file:
    ask=int(input("Enter a number: "))
    square=1
    count=0
    for ask in range(1,ask+1):
        count=count+1
        square=int(ask**2)
        print(count, square)
        write = file.write(str(count)+' '+str(square)+'\n')

