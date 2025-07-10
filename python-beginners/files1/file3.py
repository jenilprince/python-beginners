with open('para.txt', 'r') as file:
    read=file.read()
    count=1
    space=" "
    for i in read:
        if space in i:
            count=count+1
    print(count)