import timeit

# O(n^2), O(1) space
def can_two_movies_fill_flight(movie_lengths, flight_length):
    for movie1 in movie_lengths:
        for movie2 in movie_lengths:
            if movie1 != movie2 and movie1 + movie2 == flight_length:
                return True
    return False

# O(n) time, O(n) space

# Add movie lengths to a set and check to see if the
# corresponding movie length is in the set
def can_two_movies_fill_flight(movie_lengths, flight_length):
    my_set = set()
    for movie in movie_lengths:
        my_set.add(movie)
        if flight_length - movie in my_set:
            return True
    return False

# O(n) time, O(n) space
def can_two_movies_fill_flight(movie_lengths, flight_length):
    my_hash = {}

    # Hash movie lengths to its index and check to see if the flight length
    # - the current movie length is in the hash map
    for i, movie_length in enumerate(movie_lengths):
        if flight_length - movie_length in my_hash:
            return True
        else:
            my_hash[movie_length] = i
    return False

# 4.05311584473e-06
# 1.28746032715e-05

start = timeit.default_timer()
print can_two_movies_fill_flight([1, 2, 3, 4, 5, 6, 7, 8] * 100, 542)
stop = timeit.default_timer()
print stop - start
