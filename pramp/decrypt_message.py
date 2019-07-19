"""
dnotq

ord()
100, 110, 111, 116, 113

c chr(100 - 1)

x + 100 - 26n = 110

x + 214 - 26n = 111

O(i) + sum of ASCII values of previousl letter  - 26n = E[i]

O(i) = E[i] - sum of ASCII values of previous letters + 26n

100 + 114 = 214


100, 110, 111, 116, 113


sum_of_previous = 100

for i from 1 to the end:
  O[i] = E[i] - sum_of_previous

  while O[i] < ord('a'):
    O[i] += 26


  sum_of_previous += O[i]

O[0] = E[0] - 1

map()

"""

def decrypt(word):
  if not word:
    return ''

  E = [''] * len(word)
  print E

  i = 0
  for c in word:
    E[i] = c
    i += 1
  print E

  E = list(map(ord, E))
  print E

  sum_of_previous = E[0]
  print sum_of_previous


  O = [0] * len(E)
  O[0] = E[0] - 1
  print O

  for i in range(1, len(E)):
    O[i] = E[i] - sum_of_previous
    print O

    while O[i] < ord('a'):
      O[i] += 26
    print O

    sum_of_previous += O[i]

  O = list(map(chr, O))
  return ''.join(O)

word = "dnotq"
print(decrypt(word))
