x = int(input("Enter your first number: "))
y = int(input("Enter your second number: "))

print ("1. Show the even numbers between one number and another")
print ("2. Show the odd numbers between one number and another")
print ("3. Show the squares between one number and another")
print ("4. Exit the program")

choice = input("")

while True:
    if choice == '4':
        print("Thank You")
        break
#MENU

    elif choice == '1':
        for i in range(x, y):
            if(i%2==0):
                print(i, end=' ')
        print()

    elif choice == '2':
        for i in range(x, y):
            if(i%1!=0):
                print(i, end=' ')
        print()

    elif choice == '3':
        for i in range(x,y):
            i=i*i
            print(i, end=" ")

    else:
        print("Invalid Option")
        print ("1. Show the even numbers between one number and another")
        print ("2. Show the odd numbers between one number and another")
        print ("3. Show the squares between one number and another")
        print ("4. Exit the program")
        choice=input('\n ')
    continue