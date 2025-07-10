#COUNT VOWELS IN A STRING#
def vowel_count(a):
    vowels = "aeiouAEIOU"
    count = 0
    temp = a
    for i in temp:
        if i in vowels:
            count+=1
    print(count)




