#PALINDROME CHECKER#
def palindrome(num):
    string = str(num)
    reverse = ' '
    for i in string:
        reverse=i+reverse
    if int(reverse) == num:
        print(f'{num} is a palindrome')
    else:
        print(f'{num} is not a palindrome')
