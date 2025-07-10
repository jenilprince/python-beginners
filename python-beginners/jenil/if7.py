marks = int(input("Marks obtained: "))
totalmark = int(input("Total marks: "))
percent = float(marks/totalmark*100)
print(f"Percentage is {percent}%")
if percent >90:
    print("A grade")
elif percent > 80 and percent <= 90:
    print("B grade")
elif percent >70 and percent <= 80:
    print("C grade")
elif percent >60 and percent <=70:
    print("D grade")
elif percent >50 and percent <= 60:
    print("E grade")
else:
    print("Fail")

