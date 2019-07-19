# chunk([1, 2, 3, 4], 2) -> [[1, 2], [3, 4]]

# thought is just add the second argument amount of elements repeatedly
# until you reach the end

# chunk([1, 2, 3, 4, 5, 6, 7, 8], 3) -> [[1, 2, 3], [3, 4, 5], [6, 7, 8]]

# have an ind pointing to where
def chunk(arr, size):
    ind = 0
    final_arr = []
    while ind < len(arr):
        temp_arr = []
        for i in range(ind, min(ind + size, len(arr))):
            temp_arr.append(arr[i])
        final_arr.append(temp_arr)
        ind += size
    return final_arr


print chunk([1, 2, 3, 4, 5], 2)
print chunk([1, 2, 3, 4, 5, 6, 7, 8], 3)
print chunk([1, 2, 3, 4, 5, 6, 7, 8], 8)
print chunk([1, 2, 3, 4, 5, 6, 7, 8], 1)
print chunk([1, 2, 3, 4, 5, 6, 7, 8], 10)




# 1st step- clarify, constraints, corner
# runtime, spacetime constraints

# 2nd step- diagram

# 3rd step- pseudocode

# 4th step- cdoe
