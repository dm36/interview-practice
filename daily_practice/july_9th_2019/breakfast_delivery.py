# breakfast via autonomous quadcopter donres

# breakfast delivery assigned a unique ID- a positive integer

# company's 100 drones take off with a delivery- delivery ID
# is added to a list, delivery_id_confirmations

# drone comes back and lands- ID is added again to the same list

# breakfast -> 99 drones on the tarmac

# one of the drones never made it back- secret agent from Amazon
# placed an order and stole one of the drones

# find their delivery ID

# list which contains many duplicate integers and one unique integer
# find the unique integer

from collections import Counter

# storing everything in the hash map so O(n) space
# iterating through everything in the hash_map so also O(n)
# indexing is O(1)
def find_unique_integer(arr):
    my_counter = Counter(arr)
    return [key for key, val in my_counter.items() if val == 1][0]

print find_unique_integer([1, 1, 2, 2, 3])
