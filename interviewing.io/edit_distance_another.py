"""
given a misspelled string, a spell checker should return words that are "close" to the misspelled string
let's write a program to help calculate "close" words.

edit distance is defined as the number of "edits", (insertions, deletions, or substitutions) necessary to
convert one word into another.

example: car => hair = 2, one substitution to turn "c" into "h", and one insertion to add "i"
example: saturday => sundays = 4, as demonstrated below
1. saurday
2. surday
3. sunday
4. sundays

write a program that takes two strings as an input, and returns the minimum number of edits
to transform the string into the second version
"""
