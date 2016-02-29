# copy the code from sum1.py into this file, THEN:
# change your program so it keeps reading numbers until it gets a -1, then prints the sum of all numbers read
global history
history = 0
def jj(m):
    global history
    a = input("Input a number.")
    if int(a) == -1:
        return
    else:
        history = int(a) + int(history)
        jj(m)
m = 1
jj(m)
print(history)

# I don't know how to use loops to be honest;
# I've been using functions like so when loops are required.