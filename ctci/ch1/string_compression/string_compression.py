def stringCompression(x):
    char = x[0]
    count = 1
    final_str = ""

    for i in range(1, len(x)):
        if x[i] == char:
            count += 1
        else:
            final_str += char + str(count)
            char = x[i]
            count = 1

    final_str += char + str(count)
    print final_str


stringCompression("aabcccccaaa")
