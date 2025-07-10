choice =int(input("1 for c to f & 2 f to c "))
if choice==1:
    c=int(input("enter celc "))
    F = (9 / 5 * c) + 32
    print(F)
elif choice==2:
    f = int(input("enter farenheit "))
    C = (f - 32) * 5/9
    print(C)