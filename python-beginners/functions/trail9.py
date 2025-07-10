#REVERSE A STRING#
def rev(a):
    string = str(a)
    reverse=' '
    for i in string:
        reverse=i+reverse
    print(reverse)
rev("Good morning")

