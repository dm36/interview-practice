import pdb

def urlify(string, length):
    final_str = ""
    for i in range(len(string)):
        if i > (length - 1):
            break
        if string[i] == ' ':
            final_str += "%20"
        else:
            final_str += string[i]
    return final_str

# This is conceptually doing the same thing as the book
# you're looping over the Mr. John Smith array of chars backwards-
# i starts pointing to the character h whereas new_index starts
# pointing to the last whitespace- and so you're copying over non-whitespace
# characters to the end of the array and changing whitespaces (in the actual
# string not the whitespaces at the end of the string to %20)
def urlify_github(string, length):
    '''function replaces single spaces with %20 and removes trailing spaces'''
    new_index = len(string)

    for i in reversed(range(length)):
        if string[i] == ' ':
            # Replace spaces
            string[new_index - 3:new_index] = '%20'
            new_index -= 3
        else:
            # Move characters
            string[new_index - 1] = string[i]
            new_index -= 1


print urlify("Mr John Smith    ", 13)
lst = list("Mr John Smith    ")
urlify_github(lst, 13)
print lst
