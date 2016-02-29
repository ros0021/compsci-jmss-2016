# Write a program to read in words from the keyboard one at a time until the word "quit" is typed.
# Store them in a list then print them alphabetically
global history
history = []
def jj(m):
    global history
    a = input("Input a word.")
    if a == "quit":
        return
    else:
        a = str(a)
        history.append(a)
        jj(m)
m = 1
jj(m)
print(history)

# I know this code prints the list however I do not know how to sort the list alphabetically.
# I explored using things like history.sort(x) however I do not know how things like that