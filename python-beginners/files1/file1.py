with open ('original.txt', 'r') as file:
    read=file.read()
    print(read)
with open ('copy.txt', 'w') as file:
    write=file.write(read)
    