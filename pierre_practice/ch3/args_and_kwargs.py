def myfunc(a,b):
    return sum((a,b))*.05

myfunc(40,60)

# default values
def myfunc(a=0,b=0,c=0,d=0,e=0):
    return sum((a,b,c,d,e))*.05

myfunc(40,60,20)

# *args (arbitrary number of arguments), tuple of values
def myfunc(*args):
    return sum(args)*.05

myfunc(40,60,20)

# can use any word preceded by an aseterix
def myfunc(*spam):
    return sum(spam)*.05

myfunc(40,60,20)


# kwargs- dictionary of key, value pairs
def myfunc(**kwargs):
    if 'fruit' in kwargs:
        print(f"My favorite fruit is {kwargs['fruit']}")  # review String Formatting and f-strings if this syntax is unfamiliar
    else:
        print("I don't like fruit")

myfunc(fruit='pineapple')

# *args and **kwargs, args has to come first
def myfunc(*args, **kwargs):
    if 'fruit' and 'juice' in kwargs:
        print(f"I like {' and '.join(args)} and my favorite fruit is {kwargs['fruit']}")
        print(f"May I have some {kwargs['juice']} juice?")
    else:
        pass

myfunc('eggs','spam',fruit='cherries',juice='orange')

# can't place keyword arguments ahead of positional arguments
myfunc(fruit='cherries',juice='orange','eggs','spam')
