import textwrap

def wrap(string, max_width):
    i = 0
    final_str = ""
    while i < len(string):
        sub = string[i: i + max_width]
        i += max_width
        final_str += sub + "\n"
    return final_str

if __name__ == '__main__':
    string, max_width = raw_input(), int(raw_input())
    result = wrap(string, max_width)
    print result
