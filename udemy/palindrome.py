# def palindrome(str1, str2):
#     if str1 == str2[::-1]:
#         return True
#     return False

def palindrome(str1, str2):
    list_1 = list(str1)
    list_1.reverse()
    if ''.join(list_1) == str2:
        return True
    return False

print palindrome("dog", "god")
