my_file = open("numbers.txt", "r")

num1 = int(my_file.readline())
num2 = int(my_file.readline())

file_write = open("numbers.txt", "a")
print(num1 + num2, file=file_write)

my_file.close()