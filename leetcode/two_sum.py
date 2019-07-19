# iterate through each element in the array
# check if target - the present element exists in the hash map
# if it does- you've found your two sum! return the index of the present element and the previously hashed index
# if it doesn't- hash the element to its index
def two_sum(arr, target):
    hash = {}
    for i in range(len(arr)):
        if target - arr[i] in hash:
            return hash[target - arr[i]], i
        else:
            hash[arr[i]] = i

print two_sum([1, 2, 3, 4, 5], 6)
