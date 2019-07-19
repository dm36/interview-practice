# strings
s = 'hello'
print (s[1])

s = 'hello'
print (s[::-1])

print (s[-1])
print (s[4])

# lists
print ([0] * 3)

zeroes = []
for i in range(3):
    zeroes.append(0)
print (zeroes)

zeroes = [0, 0, 0]

list4 = [5, 3, 4, 6, 1]
print (sorted(list4))
list4.sort()
print (list4)

list3 = [1, 2, [3, 4, 'hello']]
list3[2][2] = 'goodbye'
print (list3)

d = {'simple_key': 'hello'}
print (d['simple_key'])

d = {'k1': {'k2': 'hello'}}
print (d['k1']['k2'])

d = {'k1': [{'nest_key': ['this is deep', ['hello']]}]}
print (d['k1'][0]['nest_key'][1][0])

d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print (d['k1'][2]['k2'][1]['tough'][2][0])

# sort a dictionary- ordered dictionary, can also sort its keys
# and values- don't think you can sort a dictionary though

# tuple(), ()
# set- all elements are unique

# false
# false
# false
# false
# false
# false

print (3.0 == 3)
