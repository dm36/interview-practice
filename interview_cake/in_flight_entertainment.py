# to implement two sum (with hash tables)-

# hash each element to its index
# check if the target element - present element is stored in the hash_map
# if it is => return True

# otherwise if you pass through the whole array return False
import timeit

def two_sum(movie_lengths, flight_length):
    hash = {}
    for index, movie_length in enumerate(movie_lengths):
        if flight_length - movie_length in hash:
            return True
        else:
            hash[movie_length] = index
    return False

# check each movie time against every other time
def another_two_sum(movie_lengths, flight_length):
    for movie1 in movie_lengths:
        for movie2 in movie_lengths:
            if movie1 + movie2 == flight_length:
                return True

# or we could sort and go through every movie length searching for the corresponding
# movie length that sums to the flight length
def binary_search(arr, elem, lo, hi):
    if lo >= hi:
        return -1
    mid = (lo + hi) / 2
    if arr[mid] == elem:
        return mid
    elif arr[mid] < elem:
        return binary_search(arr, elem, mid + 1, hi)
    else:
        return binary_search(arr, elem, lo, mid - 1)

def two_sum_binary_search(movie_lengths, flight_length):
    for ind, movie1 in enumerate(movie_lengths):
         other_ind = binary_search(movie_lengths, flight_length - movie1, 0, len(movie_lengths))
         if other_ind > -1 and other_ind != ind:
             return True
    return False

# we want to check whether two movie's lengths sum to flight_length
# so we store the movie lengths we've seen so far in a set
# and we check to see if flight_length - the present movie's length
# is in the set
def can_two_movies_fill_flights(movie_lengths, flight_length):
    movies_seen = set()
    for length in movie_lengths:
        if (flight_length - length) in movies_seen:
            return True

        movies_seen.add(length)
    return False

print two_sum([2, 7, 11, 15], 9)
print another_two_sum([2, 7, 11, 15], 9)
print

print two_sum_binary_search([2, 7, 11, 15], 9)
print two_sum_binary_search([2, 7, 11, 15], 12)
print two_sum_binary_search([2, 7, 11, 15], 26)
print two_sum_binary_search([2, 7, 11, 15], 9)
print two_sum_binary_search([2, 7, 11, 15], 18)
print two_sum_binary_search([2, 7, 11, 15], 100)
print

print can_two_movies_fill_flights([2, 7, 11, 15], 9)
print can_two_movies_fill_flights([2, 7, 11, 15], 12)
print can_two_movies_fill_flights([2, 7, 11, 15], 26)
print can_two_movies_fill_flights([2, 7, 11, 15], 9)
print can_two_movies_fill_flights([2, 7, 11, 15], 18)
print can_two_movies_fill_flights([2, 7, 11, 15], 100)

print

# Hash map
start = timeit.default_timer()
print two_sum([2]*10000, 9)
stop = timeit.default_timer()
print stop - start

# every movie time against every other time
start = timeit.default_timer()
print another_two_sum([2]*10000, 9)
stop = timeit.default_timer()
print stop - start

# binary search
start = timeit.default_timer()
print two_sum_binary_search([2]*10000, 9)
stop = timeit.default_timer()
print stop - start

# sets
start = timeit.default_timer()
print can_two_movies_fill_flights([2]*10000, 9)
stop = timeit.default_timer()
print stop - start
