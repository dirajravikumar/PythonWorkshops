name = str(input("What\'s your name?"))

name_file = open("name.txt", "w") #creates a text file called name
print("Your name is", name, file=name_file) #prints out Your name is name on the first line
name_file.close() #closes the file