import random

# You have a function rand7() that generates a random
# integer from 1 to 7. Use it to write a function rand5()
# that generates a random integer from 1 to 5.
#
# Your first thought might be to simply take the result of rand7() and take a modulus:
#
#   def rand5():
#     return rand7() % 5 + 1
#
# However, this won't give an equal probability for each possible result. We can write out each possible result from rand7() (each of which is equally probable, per the problem statement) and see that some results for rand5() are more likely because they are caused by more results from rand7():
#
# rand7()	rand5()
# 1	2
# 2	3
# 3	4
# 4	5
# 5	1
# 6	2
# 7	3
# So we see that there are two ways to get 2 and 3, but only one way to get 1, 4, or 5. This makes 2 and 3 twice as likely as the others.

# Re-roll when we get a number greater than 5 so each integer
# has a 1/7 probability of being picked

# Worst case O(infinity) time

def rand5():
    random_num = float("inf")
    while random_num > 5:
        random_num = random.randint(1, 7)
    print random_num


rand5()
