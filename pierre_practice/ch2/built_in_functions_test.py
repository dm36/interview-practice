# def word_lengths(phrase):
#     words = phrase.split(' ')
#     print map(lambda x: len(x), words)

def word_lengths(phrase):
    print map(len, phrase.split())

word_lengths('How long are the words in this phrase')

from functools import reduce

def digits_to_num(digits):
    print reduce(lambda x, y: (10 * x) + y, digits)

digits_to_num([3,4,3,2,1])

def filter_words(word_list, letter):
    print filter(lambda x: x.startswith('h'), word_list)

l = ['hello','are','cat','dog','ham','hi','go','to','heart']
filter_words(l,'h')

def concatenate(L1, L2, connector):
    print [num1 + connector + num2 for num1, num2 in zip(L1, L2)]
concatenate(['A','B'],['a','b'],'-')

def d_list(L):
    return {value: key for key, value in enumerate(L)}

print d_list(['a','b','c'])

def count_match_index(L):
    return len([num for num, index in enumerate(L) if num == index])

# count of the number of times whose value matches its index
print (count_match_index([0,2,2,1,5,5,6,10]))
