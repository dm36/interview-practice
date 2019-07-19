# Go through the array and swap adjacent elements
# if the present element is greater than the next element-
# repeat this process until you swap 0 elements in a single
# pass of the array
def count_swaps(s):
    is_sorted = False
    count = 0
    while not is_sorted:
        is_sorted = True
        for i in range(len(s)-1):
            if s[i] > s[i+1]:
                temp = s[i]
                s[i] = s[i+1]
                s[i+1] = temp
                is_sorted = False
                count += 1
    print "Array is sorted in " + str(count) + " swaps"
    print "First Element: " + str(s[0])
    print "Last Element: " + str(s[-1])

count_swaps([1, 2, 3])
count_swaps([3, 2, 1])
