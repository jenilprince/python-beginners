try:
    with open('data.txt', "w") as f:
        f.write("Hello World\n")
        f.write("1234")
    with open('data.txt', "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found!")
finally:
    print("Execution complete")