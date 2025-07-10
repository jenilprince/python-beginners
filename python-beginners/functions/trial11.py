#NO. OF WORDS IN A SENTENCE#
def word_count(word):
    count = 1
    for i in word:
        if i == " " or i == ".":
            count+=1

    print(count)
