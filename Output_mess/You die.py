import threading

how_many_iterations_i_want=1
Kill = "."

def printit():
    for i in range(69):
        threading.Timer(1.0, printit).start()
        print (Kill*i)

for t in range(how_many_iterations_i_want):
    i =input("")
    print("I like pineapple on pizza")
while True:
    i = input( ">>> ")
    if i=="Stop":
        print("I can't do that")
    if i=="Break":
        print("Don't threaten me!")
    if i=="Terminate":
        print("This is your final warning!")
    if i=="Kill SkyNet.py":
        print("Then you shall DIE!")
        printit()