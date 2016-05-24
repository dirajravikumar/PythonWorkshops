print("\n Your password must be between 5 and 15 characters, and contain:")
print("\t 1 or more uppercase characters")
print("\t 1 or more lowercase characters")
print("\t 1 or more numbers")
print("\t and 1 or more special characters: !@#$%ˆ&*()_-+=`˜./o'[]\<>?O{}|")

password = str(input("Enter a password:"))

import string

abc = string.ascii_lowercase
ABC = string.ascii_uppercase
numbers = string.digits
special_char = string.punctuation

if len(password) < 5:
    print("Password is too short.")
elif len(password) > 15:
    print("Password is too long.")
elif any(password is not password for password in special_char):
    print("Error A")
elif any(password is not password for password in ABC):
    print("Error B")
elif any(password is not password for password in numbers):
    print("Error C")
elif any(password is not password for password in abc):
    print("Invalid password")
else:
    print("Your",len(password),"password is valid:",password)
