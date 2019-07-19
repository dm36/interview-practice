str1 = "aaaabcccaa"
# str2 = "3e4f2e"

# store character and count
# once we arrive at a new character we add the character and the count
# to the string and reset
# make sure to do it after the for loop too
def encode(string):
    final_str = ""
    saved_char = string[0]
    count = 1

    for char in string[1:]:
        if char == saved_char:
            count += 1
        if char != saved_char:
            final_str += str(count) + saved_char
            saved_char = char
            count = 1
    final_str += str(count) + saved_char

    return final_str

encode(str1)

# parse count and character and add that many to the final string


def decode(string):
    # it = iter(string)
    # for x in it:
    #     print x, next(it)

    # retrieve all the nums and the chars
    nums = [string[i] for i in range(len(string)) if i % 2 == 0]
    chars = [string[i] for i in range(len(string)) if i % 2 == 1]
    final_string = ""

    # zip up the nums and chars
    for num, char in zip(nums, chars):
        final_string += int(num) * char

    return final_string

print decode("3e4f2e")
print decode(encode(str1))

# https://www.youtube.com/watch?v=WepWFGxiwRs
# word break dp
