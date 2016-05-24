color_names = {
    "AliceBlue": "#f0f8ff",
    "AntiqueWhite":"#faebd7",
    "AquaMarine":"#7fffd4",
    "Azure":"#f0ffff",
    "Beige":"#f5f5dc",
    "Bisque":"#ffe4c4",
    "Black":"#000000",
    "Blue":"#0000ff",
    "Brown":"#a52a2a",
    "Chartreuse":"#7fff00"
}

color = input("Enter a color name: ")
while color != "":
    if color in color_names:
        print(color, "is", color_names[color])
    else:
        print("Color not found.")
    color = input("Enter a color name: ")