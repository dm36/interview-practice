# start, stop, step size
print (range(0, 11))
print (list(range(0, 11)))
print (list(range(0, 11, 2)))
print (list(range(0, 101, 10)))

for i, letter in enumerate('abcde'):
    print ('At index {} the letter is {}'.format(i, letter))

# can call list on the result of enumerate
print (list(enumerate('abcde')))

my_list_1 = ['swag', 'swagger', 'swags']
my_list_2 = ['dhruv', 'shrub', 'shrubby']

print (list(zip(my_list_1, my_list_2)))

for word1, word2 in zip(my_list_1, my_list_2):
    print (word1, word2)

from random import shuffle

mylist = [1, 2, 3, 4, 5, 6]
shuffle(mylist)

print (mylist)

from random import randint
print (randint(0, 100))
