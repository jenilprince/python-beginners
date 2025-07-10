with open('data.txt', 'r') as file:
    word=input('Enter a word: ')
    read=file.read()
    if word in read:
        print("Found")
    else:
        print("Not Found")
