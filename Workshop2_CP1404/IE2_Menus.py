name = str(input("Enter name:"))
print("(H)ello")
print("(G)oodbye")
print("(Q)uit" )

choice = input("")

#import sys

while True:
    if choice == 'Q' or choice == 'q':
        print("Finished")
        break
#MENU

    elif choice == 'H' or choice == 'h':
        print("Hello",name,"\n" )
        print("(H)ello")
        print("(G)oodbye")
        print("(Q)uit\n" )
        choice=input('\n ')

    elif choice == 'G' or choice == 'g':
        print("Goodbye", name)
        print("(H)ello")
        print("(G)oodbye")
        print("(Q)uit\n" )
        choice=input('\n ')
    else:
        print("Invalid Option")
        print("(H)ello")
        print("(G)oodbye")
        print("(Q)uit\n" )
        choice=input('\n ')
    continue