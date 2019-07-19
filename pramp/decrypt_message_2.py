# Specification:
#  - all latin lowercase letters (a-z)
#
# ascii value range a: 97, z: 97 + 25 = 122
#
# decrypt
#
# - decrypt the first letter c:
#    convert c to its ASCII value n
# .  if n == 97 == 123 - 26, then return z,
# .  if n == 98, then return a,
# .
# - to decrypt the next letter c2
# .  add 26 to c2 until the value n2 - previous value is between
# .  98 and 123
# .  then subtract 1 to get the ASCII value of the 2nd character
# .
# test case:
# 1.
#   input: word == ''
#   output: ''
#
# 2.
# . input: word == 'dnotq'
#   output: 'crime'
#
# 3.
#   input:  word = "flgxswdliefy"
#   output: "encyclopedia"
#
# run test cases
# 2. dnotq
#
#    d -> 100 = step3
#    98 <= step3 - 0 <= 123
#    prev2 = 100
# .  characters = [chr(99)] = ['c']
#
# .  n -> 110 = step3
# .  110 + 26 * 4 = 110 + 104 = 214 - 100 = 114
# .  prev2 = 214
# .  characters = ['c', char(113)] = ['c', ]

def decrypt(word):
  # Null case
  if not word:
    return ''

  characters = list()
  previous_step_2_encoded_value = 1
  for c in word:
    step3_encoded_value = ord(c)
    # Want to increase step3_encoded_value by 26 until the difference after
    # subtract the previous_step_2_encoded_value is between 98 and 123
    while not (97 <= (step3_encoded_value - previous_step_2_encoded_value) <= 122):
      step3_encoded_value += 26
    char_ascii = step3_encoded_value - previous_step_2_encoded_value
    previous_step_2_encoded_value = step3_encoded_value
    characters.append(chr(char_ascii))
  return ''.join(characters)
