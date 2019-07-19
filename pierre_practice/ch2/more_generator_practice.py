# def gencubes(n):
#     for num in range(n):
#         yield num**3
#
# for x in gencubes(10):
#     print (x)


# 0, 1, 1, 2, 3, 5, 8, 13, 21
def genfib(n):
    a, b = 1, 1
    for num in range(n):
        yield a
        a, b = b, a + b

for x in genfib(10):
    print (x)

def simple_gen():
    for x in range(3):
        yield x

# StopIteration error- all our values
# have been yielded
g = simple_gen()
print (next(g))
print (next(g))
print (next(g))
# print (next(g))

s = 'hello'
for let in s:
    print (let)

# iterator for s- have to save it away
print (type(s))
my_iter = iter(s)
print (type(s))
print (type(my_iter))
print next(my_iter)
print next(my_iter)
print next(my_iter)
print next(my_iter)
print next(my_iter)
