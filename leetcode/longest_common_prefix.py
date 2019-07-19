def longest_common_prefix(strings):
    index = 1
    last_prefix = ""
    prefix = ""

    len_strings = [len(string) for string in strings]
    min_len = min(len_strings)

    while index <= min_len:
        last_prefix = prefix
        prefix = strings[0][:index]

        print last_prefix, prefix

        for i in range(1, len(strings)):
            if prefix != strings[i][:index]:
                return last_prefix
        index += 1

# print longest_common_prefix(["flower", "flow", "flight"])
# print longest_common_prefix(["dog", "racecar", "car"])
# print longest_common_prefix(["a", "b"])
print longest_common_prefix(["aa", "a"])

# print longest_common_prefix(["", ""])
