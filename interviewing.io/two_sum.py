# O(n^2)
def two_sum(lst, k):
    two_sums = []
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i != j:
                if lst[i] + lst[j] == k:
                    two_sums.append(lst[i], lst[j])
    return two_sums


def two_sum_opt(lst, k):
    dict = {}
    two_sums = []
    for i in range(len(lst)):
        if k - lst[i] in dict.keys():
            two_sums.append((lst[i], (k - lst[i])))
        else:
            dict[lst[i]] = i

    print two_sums

def two_sum_set(lst, k):
    lst_set = set(lst)
    num_lst = list(lst_set)
    two_sums = []
    for num in num_lst:
        lst_set.remove(num)

        if k - num in lst_set:
            two_sums.append((num, k - num))

    print two_sums

# Can also do a two pointer approach, and also use binary search
two_sum_opt([1, 3, 2, 5, 46, 6, 7, 4], 5)

two_sum_set([1, 3, 2, 5, 46, 6, 7, 4], 5)
