def swap_case(s):
    final_str = ""
    for char in s:
        if char.islower():
            final_str += char.upper()
        elif char.isupper():
            final_str += char.lower()
        else:
            final_str += char
    return final_str


if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print result
