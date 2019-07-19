input = [1, 4, 3, 2]

# def arrayPairSum(nums):
#     nums.sort()
#     i = 0
#     sum = 0
#
#     while i < len(nums):
#         sum += min(nums[i], nums[i+1])
#         i += 2
#     return sum

def arrayPairSum(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    # splicing it as such means that you take
    # the first of every two numbers
    print sorted(nums)
    print sorted(nums)[::2]
    # return sum(sorted(nums)[::2])

print arrayPairSum(input)
