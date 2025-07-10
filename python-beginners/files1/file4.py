try:
    with open('sample1.txt', 'r') as file:
        print(file.read())
except FileNotFoundError:
    print("File not found")
