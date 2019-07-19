def steps(num):
    for i in range(1,  num + 1):
        print ('#' * i) + ('d' * (num - i))

steps(4)
