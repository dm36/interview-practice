def oddNumbers(l, r):
    arr = []
    if l % 2 == 1:
        pass
    else:
        l = l + 1

    for i in range(l, r+1, 2):
        arr.append(i)
    print arr


oddNumbers(3, 9)
