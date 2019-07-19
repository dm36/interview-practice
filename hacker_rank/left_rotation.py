def rotateOnce(a):
    temp = a[0]
    for i in range(len(a)-1):
        a[i] = a[i+1]
    a[-1] = temp
    return a

def rotLeft(a, d):
    for _ in range(d):
        rotateOnce(a)
        print a

def array_left_rotation(a, k):
    # [5] + [1, 2, 3, 4]
    return a[k:]+a[:k]

rotLeft([1, 2, 3, 4, 5], 4)

print array_left_rotation([1, 2, 3, 4, 5], 4)
