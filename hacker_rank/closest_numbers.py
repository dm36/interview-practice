def closest_numbers(arr):
    min_diff = float("inf")
    elems = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j:
                if abs(arr[j] - arr[i]) < min_diff:
                    min_diff = abs(arr[j] - arr[i])

    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j:
                if abs(arr[j] - arr[i]) == min_diff:
                    if arr[i] < arr[j] and (arr[i], arr[j]) not in elems and (arr[j], arr[i]) not in elems:
                        elems.append((arr[i], arr[j]))
                    elif (arr[j], arr[i]) not in elems and (arr[i], arr[j]) not in elems:
                        elems.append((arr[j], arr[i]))

    elems.sort()
    for i in range(len(elems)):
        print elems[i][0], elems[i][1]

closest_numbers([6, 2, 4, 10])
