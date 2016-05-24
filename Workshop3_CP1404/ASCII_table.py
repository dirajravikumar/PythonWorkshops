lower = 10
upper = 100
user_input = int(input("Enter a number ({}---{}):".format(lower,upper)))

for i in range(user_input, 120, 11):
    print("{} {}".format(i, chr(i)).strip())
