import csv
with open("l.csv", "w") as f:
    write=csv.writer(f)
    write.writerow(["Name","Age", "Class", "Height"])
    write.writerow(["Jenil", 18, 12, 175])
    write.writerow(["Abc", 21, 0, 594])
with open("l.csv", "r") as f:
    read=csv.reader(f)
    for any_row in read:
        next(read)
        print(any_row)

