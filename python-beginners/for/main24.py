# CHECK PALINDROME OR NOT #
num = int(input("Number : "))
string = str(num)
reverse = ' '
for i in string:
    id = i
    reverse = id + reverse
print(f"Reversed == {reverse}")
if num == int(reverse):
    print("Palindrome")
else:
    print("Not Palindrome")

