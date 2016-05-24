import random

VOWELS = "AEIOU"
CONSONANTS = "BCDFGHIJKLMNPQRSTVWXYZ"

word_format = "CCVC"
word = ""
for kind in word_format:
    if kind == "C":
        word += random.choice(CONSONANTS)
    else:
        word += random.choice(VOWELS)

print(word.lower())