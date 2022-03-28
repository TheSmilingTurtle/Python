import math
num = 1
l = []

while len(l) < 2:
    f = num**2
    g = f**(1/3)
    if not num%1000000:
        print("ran lap")
    if math.floor(g) == g:
        print(f)
        l.append([f,num,g])
    num += 1