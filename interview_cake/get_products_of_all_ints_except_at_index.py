# O(n^2) time, O(n) space
def get_products_of_all_ints_except_at_index(ints):
    prods = []
    for i in range(len(ints)):
        prod = 1
        for j in range(len(ints)):
            if j == i:
                continue
            else:
                prod *= ints[j]
        prods.append(prod)
    print prods

# O(n) time, O(n) space
def get_products_of_all_ints_except_at_index(ints):
    prod_so_far = 1
    prods = []
    for i in range(len(ints)):
        prods.append(prod_so_far)
        prod_so_far *= ints[i]
    print prods

    prod_so_far_reversed = 1
    prods_reversed = []
    for i in range(len(ints)-1, -1, -1):
        prods_reversed.append(prod_so_far_reversed)
        prod_so_far_reversed *= ints[i]
    print prods_reversed

    final_prods = []
    for i in range(len(prods)):
        final_prods.append(prods[i] * prods_reversed[len(prods)-i-1])
    print final_prods

# O(n) time, O(n) space but we saved a list
def get_products_of_all_ints_except_at_index_compact(ints):
    prods_so_far = 1
    prods = [1] * len(ints)

    for i in range(len(ints)):
        prods[i] = prods_so_far
        prods_so_far *= ints[i]
    print prods
    prods_so_far = 1
    for i in range(len(ints)-1, -1, -1):
        prods[i] *= prods_so_far
        prods_so_far *= ints[i]
    return prods

def productExceptSelf(self, nums):
    prods_so_far = 1
    # prods = [1] * len(nums)
    prods = []

    for i in range(len(nums)):
        prods.append(prods_so_far)
        prods_so_far *= nums[i]

    prods_so_far = 1
    for i in range(len(nums)-1, -1, -1):
        prods[i] *= prods_so_far
        prods_so_far *= nums[i]
    return prods

# get_products_of_all_ints_except_at_index([1, 7, 3, 4])
# get_products_of_all_ints_except_at_index([0, 0, 0, 0])
# get_products_of_all_ints_except_at_index([1])
print get_products_of_all_ints_except_at_index_compact([1, 7, 3, 4])
