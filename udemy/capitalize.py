def capitalize(sentence):
    words = sentence.split(" ")
    print words
    upper_case_words = [word[0].upper() + word[1:] for word in words]
    print ' '.join(upper_case_words)

sentence = "a short sentence"
print capitalize(sentence)
