import csv
with open("l.csv", "w") as file:
    a=csv.writer(file)
    a.writerow(["name","age"])
    a.writerow(["alen",19])
    a.writerow(["jenil",18])
with open("l.csv", "r") as file:
    r=csv.reader(file)
    for a in r:
        next(r)
        print(a)