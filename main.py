#asks user for a color
color = input("Input a color: ")

#outputs results based on color selected
if color == "yellow" or color == "blue":
    print("Mid color.")
elif color == "green" or color == "red":
    print("Good color.")
elif color == "pink" or color == "purple":
    print("Ok color.")
elif color == "black" or color == "white":
    print("GOATED color.")
#if anything else it says invalid
else:
    print("Invalid.")
