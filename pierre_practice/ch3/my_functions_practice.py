import math

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# start at an odd number
# and
def is_prime_better(num):
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True


print (is_prime(3))
print (is_prime(51))
print (is_prime(41))

print (is_prime_better(3))
print (is_prime_better(51))
print (is_prime_better(41))
