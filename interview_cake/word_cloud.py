from collections import Counter

def word_cloud(str):
    arr = str.split(" ")
    print arr

    # Fix .s and commas at the end of a word
    for ind, word in enumerate(arr):
        if word[-1].isalpha() == False:
            arr[ind] = word[:-1]

    print Counter(arr)

word_cloud("After beating the eggs, Dana read the next step: Add milk and eggs, then add flour and sugar.")
