#EVEN OR ODD CHECKER#
def check(a):
    if a==0:
        print(f"{a} is invalid")
    elif a%2==0:
        print(f"{a} is even")
    elif a%2==1:
        print(f"{a} is odd")

check(4)