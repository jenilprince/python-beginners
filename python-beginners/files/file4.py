import csv
with open('list.csv', 'w') as file:
    write = csv.writer(file)
    write.writerow(["apple"])
    write.writerow(["banana"])
    write.writerow(["mango"])
with open('list.csv', 'r') as file:
    read=csv.reader(file)
    for row in read:
        next(read)
        print(row)

