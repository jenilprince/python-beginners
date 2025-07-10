#MAX OF 3 NO.S #
def max(a,b,c):
    if a>b and a>c:
        print(f"{a} (1st) is the greatest")
    elif b>c and b>a:
        print(f"{b} (2nd) is the greatest")
    else:
        print(f"{c} (3rd) is the greatest")
max(1,2,3)
