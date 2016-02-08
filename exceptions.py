bubba = True
while bubba:
    try:
        x = input("Type a big juicy whole number.\n")
        x = int(x)
        bubba = False
        print ("Yeah good job you did it nice congratulations good effort nice job thats pretty cool man bomb diggity you typed a", x)
    except ValueError:
        print ("What in the hell is '", x, "' are you stupid try again")
print ("A WOWIE")