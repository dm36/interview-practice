# map function
def square(num):
    return num ** 2

my_nums = [1, 2, 3, 4]
# function comes first and then the list
print (map(square, my_nums))

print (list(map(square, my_nums)))

# returns even if the string has an even # of chars
# othewise returns the first character in the string
def splicer(my_string):
    if len(my_string) % 2 == 0:
        return 'even'
    else:
        return my_string[0]

mynames = ['John', 'Cindy', 'Sarah', 'Kelly', 'Mike']
print (list(map(splicer, mynames)))

# filter
def check_even(num):
    return num % 2 == 0

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print (filter(check_even, nums))

print (list(filter(check_even, nums)))

# lambda expression
def square(num):
    result = num**2
    return result

print (square(2))

def square(num): return num**2

print (square(2))
square = lambda num: num **2
square(2)

print (list(map(lambda num: num **2, nums)))

print (list(map(lambda num: num * 2, nums)))

print (list(map(lambda num: num % 2 == 0, nums)))

lambda s: s[0]

lambda s: s[::-1]

lambda x, y: x + y
