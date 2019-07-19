# def reverse(str):
#     return str[::-1]

# def reverse(str):
#     arr = list(str)
#     arr.reverse()
#     return ''.join(arr)

def reverse(str):
    arr = list(str)
    i, j = 0, len(arr) - 1
    while i < j:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        i += 1
        j -= 1
    return ''.join(arr)

print reverse("swag")
