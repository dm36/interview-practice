def number_of_vowels(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for char in str:
        if char in vowels:
            count += 1
    return count

print number_of_vowels("aeiou")
print number_of_vowels("abcdef")
