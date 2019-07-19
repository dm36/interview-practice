# Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.
#
# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
#
# If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

# http://book.pythontips.com/en/latest/map_filter.html
def order(sentence):
    words = sentence.split()
    # pulls the digit out of each word
    print [int(filter(str.isdigit, x)) for x in words]

    # sort words based on the digit in each of them
    return " ".join(sorted(sentence.split(), key=lambda x: int(filter(str.isdigit, x))))

# def order(words):
#     print words.split()
#     print [sorted(w) for w in words.split()]
#     print sorted(words.split(), key = lambda w:sorted(w))
#
#     # split the words on whitespace, sort by the digit in each word
#     # and join the words back together
#     return ' '.join(sorted(words.split(), key=lambda w:sorted(w)))

# def order(sentence):
#     words = sentence.split(" ")
#     word_location = []
#     for word in words:
#         for char in word:
#             if char.isdigit():
#                 word_location.append((word, int(char)))
#                 break
#
#     # in place
#     word_location.sort(key = lambda word: word[1])
#     return ' '.join([word for word, count in word_location])
#
    # not in place
    # print sorted(word_location, key = lambda word: word[1])


print order("is2 Thi1s T4est 3a")
