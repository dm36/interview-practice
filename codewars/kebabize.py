import re
def first_word(string):
    for i, char in enumerate(string):
        if char.isupper():
            return string[:i]

def kebabize(string):
    # remove digits from the string
    string = ''.join([char for char in string if not char.isdigit()])
    first_string = ""

    # want to pull the first word if the first word can be represented
    # as lowercase
    if string[0].islower():
        first_string = first_word(string)

    # array of the upper case strings
    camel_strings = re.findall("[A-Z][^A-Z]*", string)

    # convert array to lower-case
    lower_case_strs = [str[0].lower() + str[1:] for str in camel_strings]

    # insert the first string into the lower case strings
    if first_string != "":
        lower_case_strs.insert(0, first_string)

    # join on -
    return '-'.join(lower_case_strs)

# https://stackoverflow.com/questions/2277352/split-a-string-at-uppercase-letters

print kebabize('myCamelCasedString')
print kebabize('myCamelHas3Humps')
print kebabize('SOS')
# kebabize('42')
print kebabize('CodeWars')
