import string

def add_word(one_word, text_dict):
    if one_word not in text_dict:
        text_dict[one_word] = 1
    else:
        text_dict[one_word] += 1

def process_line(text_line, text_dict):
    word_list = text_line.split()
    for word in word_list:
        word = word.strip(string.punctuation)
        add_word(word, text_dict)

text_dict = {} # defining a new dictionary
text_line = str(input("Text: "))
process_line(text_line, text_dict)

for word in sorted(text_dict):
    print("{} : {}".format(word, text_dict[word]))