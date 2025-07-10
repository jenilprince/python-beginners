#COUNT DIGITS IN A NUMBER#
def count(num):
    string = str(num)
    count = 0
    for i in string:
        count += 1
    print(f'Digit Count == {count}')


