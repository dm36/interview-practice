from collections import Counter
from collections import defaultdict

# def k_most_frequent(nums, k):
#     counter = Counter(nums)
#     most_common = counter.most_common(k)
#     return [num for num, count in most_common]

# O(nlogn) runtime to sort based on freq, O(n) space to build the freq map
def k_most_frequent(nums, k):
    # build freq map
    freq_map = defaultdict(int)
    for num in nums:
        freq_map[num] += 1

    # sort in descending order based on frequency
    sorts = sorted(zip(freq_map.values(), freq_map.keys()), reverse=True)

    # get the first k nums with the highest frequency
    return [num for freq, num in sorts[:k]]

print (k_most_frequent([1,1,1,2,2,3], 2))
print (k_most_frequent([1], 1))
print (k_most_frequent([1, 1, 2, 2, 3, 3], 3))


# /*
#
# Given a non-empty array of integers, return the k most frequent elements.
#
# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
#
# Example 2:
# Input: nums = [1], k = 1
# Output: [1]
#
# Note: Assume k is always valid. The input array will always have k unique most frequent elements.
#
# For example, if nums = [1, 1, 2, 2, 3, 3], k *cannot* be 2 because there are no 2 unique most
# frequent elements. In this example, the only valid k is 3.
#
# */
