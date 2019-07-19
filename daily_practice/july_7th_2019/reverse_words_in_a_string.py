def reverse_words(s):
    arr_of_words = s.split()
    arr_of_words.reverse()
    return ' '.join(arr_of_words)

s = "the sky is blue"
print reverse_words(s)

def split(s):
    final_arr = []
    for i in range(len(s)):
        final_arr.append(s[i])
    return final_arr


print split("hello")
