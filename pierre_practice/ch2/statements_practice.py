st = 'Print only the words that start with s in this sentence'
print ([word for word in st.split() if word.startswith('s')])
print ([word for word in st.split() if word[0] == 's'])
print (list(range(0, 11, 2)))

print ([i for i in range(1, 51) if i % 3 == 0])

st = 'Print every word in this sentence that has an even number of letters'
for word in st.split():
    if len(word) % 2 == 0:
        print ('even!')

for i in range(1, 100):
    if i % 3 == 0:
        print ('Fizz')
    elif i % 5 == 0:
        print ('Buzz')
    elif i % 3 == 0 and i % 5 == 0:
        print ('FizzBuzz')

st = 'Create a list of the first letters of every word in this string'
print ([word[0] for word in st.split()])
