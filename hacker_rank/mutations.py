def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]

if __name__ == '__main__':
    s = raw_input()
    i, c = raw_input().split()
    s_new = mutate_string(s, int(i), c)
    print s_new

# def mutate_string(string, position, character):
#     lst = list(string)
#     lst[position] = character
#     return ''.join(lst)
#
#
# if __name__ == '__main__':
#     s = raw_input()
#     i, c = raw_input().split()
#     s_new = mutate_string(s, int(i), c)
#     print s_new
