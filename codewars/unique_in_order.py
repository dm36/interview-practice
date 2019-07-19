def unique_in_order(iterable):
    current_char = ""
    uniq = []

    for char in iterable:
        if char != current_char:
            current_char = char
            uniq.append(char)
        else:
            continue
    return uniq


print unique_in_order('AAAABBBCCDAABBB')
print unique_in_order('ABBCcAD')

# def unique_in_order(iterable):
#     result = []
#     prev = None
#     for char in iterable[0:]:
#         if char != prev:
#             result.append(char)
#             prev = char
#     return result

# from itertools import groupby
#
# def unique_in_order(iterable):
#     return [k for (k, _) in groupby(iterable)]
