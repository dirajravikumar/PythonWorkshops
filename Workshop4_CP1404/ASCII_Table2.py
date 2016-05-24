def get_number():
    lower = int(input("Enter a number:"))
    upper = int(input("Enter a number more than {}:".format(lower)))
    while True:
        if upper > lower:
            break
        print("Upper value too low!")
        upper = int(input("Enter a number more than {}:".format(lower)))
    for i in range(lower, upper,):
        print("{} {}".format(i, chr(i)).strip())

get_number()