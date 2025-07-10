with open('log.txt', 'a') as file:
    append=file.write("Program started\n")
with open('log.txt', 'r') as file:
    print(file.read())
