def steps(count):
    for i in range(1, count + 1):
        print ('#' * i) + ('x' * (count - i))

steps(4)

# first line should be just a single # and a whitespace
# second line should be two ##
