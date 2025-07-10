##HARSHAD NUMBER##
numb = int(input("Enter a number: "))
temp = numb
sumdig=0
while numb!=0:
    lastdig = numb%10
    sumdig+=lastdig
    numb=numb//10
if (temp%sumdig == 0):
    print("Harshad number")
else:
    print("Not a Harshad number")
