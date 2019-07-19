# input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
# print input
# arr = input.split("\n")
# print arr
#
# # index, tab count and string (without whitespaces) for files
# ext_array = [(i, my_str.count('\t'), my_str.strip()) for i, my_str in enumerate(arr) if "." in my_str]
#
# # building up a path backwards from the file -> beginning directory
# my_len = 0
# for i, tab_count, my_str in ext_array:
#     final_str = my_str
#     my_tab_count = tab_count
#
#     # as long as tab count
#     for j in range(i, -1, -1):
#         if "." not in arr[j] and arr[j].count('\t') < my_tab_count:
#             final_str += '/' + arr[j].strip()
#             my_tab_count = arr[j].count('\t')
#
#     # update max length
#     if len(final_str) > my_len:
#         my_len = len(final_str)
#
# return my_len
# print final_str

# idea is to map each depth to the length of the directory path
# at that depth (with the )
# and everytime you observe a file add the stored di
def lengthLongestPath(input):
    for l














# def lengthLongestPath(input):
#     maxlen = 0
#     pathlen = {0: 0}
#     for line in input.splitlines():
#         # remove tabs from the left
#         name = line.lstrip('\t')
#         # depth is the # of tabs
#         depth = len(line) - len(name)
#
#         # we add the length to a file to the length to a subdirectory
#         if '.' in name:
#             maxlen = max(maxlen, pathlen[depth] + len(name))
#
#         # records the pathlen at all depths
#         # i.e. the length to a subdirectory
#         else:
#             pathlen[depth + 1] = pathlen[depth] + len(name) + 1
#     return maxlen

print (lengthLongestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"))
