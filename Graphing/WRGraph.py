import matplotlib.pyplot as plt
import math

try:
    n = input("Enter country: ").lower()
except:
    pass

b = True

if n:
    if n[0] == "s":
        l = [0,8]
        f = [4,0]
        g = [0,8]
        h = [8,0]
        c = "Schweiz"
    elif n[0] == "j":
        l = [0,10]
        f = [10,0]
        g = [0,20]
        h = [10,0]
        c = "Japan"
    else:
        print("You didn't enter a valid query")
        b = False
else:
    print("You didn't enter a query")
    b = False

if b:
    plt.xlim(0,20)
    plt.ylim(0,20)
    plt.title(c)
    plt.ylabel("Handys")
    plt.xlabel("Medikamente")
    plt.plot(l,f, label="Transformationskurve")
    plt.plot(g,h,linestyle='dashed', label="Tauschlienie")
    plt.legend()
    plt.show()