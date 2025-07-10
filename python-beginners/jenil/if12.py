phy = int(input("Physics marks: "))
che = int(input("Chemistry marks: "))
mat = int(input("Mathematics marks: "))
bio = int(input("Biology marks: "))
com = int(input("Computer marks: "))
percent = (phy + che + mat + bio + com)/500*100
if percent >= 90:
    print("Grade A")
elif percent >= 80:
    print("Grade B")
elif percent >= 70:
    print("Grade C")
elif percent >= 60:
    print("Grade D")
elif percent >= 40:
    print("Grade E")
elif percent < 40:
    print("Grade F")