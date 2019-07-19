import random
def squares(N):
    for i in range(N):
        yield i**2

for num in squares(16):
    print num

def rand(N, low, high):
    for i in range(N):
        yield random.randint(low, high)

for num in rand(10, 1, 10):
    print num

s = 'hello'
iter = iter(s)
print next(iter)
print next(iter)
print next(iter)
print next(iter)
print next(iter)

my_list = [1,2,3,4,5]

gencomp = (item for item in my_list if item > 3)

for item in gencomp:
    print(item)
