import random

alphabets = "abcdefghijklmnopqrstuvwxyz"
Alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
special_char = "!@#$%^&*()_-=+`~,./o'[]\<>?O{}|"

password_format = "aAnsaAns"
password = ""
for kind in password_format:
    if kind == "a":
        password += random.choice(alphabets)
    elif kind == "A":
        password += random.choice(Alphabets)
    elif kind == "n":
        password += random.choice(numbers)
    else:
        password += random.choice(special_char)

print(password)