with open("user_info.txt","w") as file:
    name=input("Enter your name: ")
    file.write(name+"\n")
    age=input("Enter your age: ")
    file.write(age+"\n")
with open("user_info.txt","r") as file:
    print(file.read())