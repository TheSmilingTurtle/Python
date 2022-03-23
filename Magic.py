import time
import math

l = []
try:   
    n  = int(input(">>>"))
except:
    pass

def printer(l):
    x = 0
    for i in range(0,len(l)):
        a = []
        for j in range(0,len(l)):
            a.append(l[j][i])
        print(a)
    for i in range(len(a)):
        x += a[i]
    print("The sum of the sides equals", x)

def lgen():
    l = [[None for i in range(0,n)]
            for j in range(0,n)]
    return l

def double_even(n):
    f = 0
    for j in range(0,len(l)):
        for i in range(0,len(l)):
            f += 1
            if ((i < n/4 and j < n/4) or (i >= 3*n/4 and j >= 3*n/4) or (i < n/4 and j >= 3*n/4) or (i >= 3*n/4 and j < n/4)) or (i < 3*n/4 and i >= n/4 and j < 3*n/4 and j >= n/4):
                l[i][j] = f

    f = 0
    for j in range(0,len(l)):
        for i in range(0,len(l)):
            if not l[i][j]:
                l[i][j] = (n**2)-f
            f += 1

def odds(s):
    if s % 2 == 0:
        s += 1
    q = [[0 for j in range(s)] for i in range(s)]
    p = 1
    i = s // 2
    j = 0
    while p <= (s * s):
        q[i][j] = p
        ti = i + 1
        if ti >= s: ti = 0
        tj = j - 1
        if tj < 0: tj = s - 1
        if q[ti][tj] != 0:
            ti = i
            tj = j + 1
        i = ti
        j = tj
        p = p + 1
 
    return q, s
 
def singly_even(s):
    if s % 2 == 1:
        s += 1
    while s % 4 == 0:
        s += 2
 
    q = [[0 for j in range(s)] for i in range(s)]
    z = s // 2
    b = z * z
    c = 2 * b
    d = 3 * b
    o = odds(z)
 
    for j in range(0, z):
        for i in range(0, z):
            a = o[0][i][j]
            q[i][j] = a
            q[i + z][j + z] = a + b
            q[i + z][j] = a + c
            q[i][j + z] = a + d
 
    lc = z // 2
    rc = lc
    for j in range(0, z):
        for i in range(0, s):
            if i < lc or i > s - rc or (i == lc and j == lc):
                if not (i == 0 and j == lc):
                    t = q[i][j]
                    q[i][j] = q[i][j + z]
                    q[i][j + z] = t
    return q

t0 = time.time()
l = lgen()
if n%2:
    l, f = odds(n)
elif not n%2 and not n%4:
    double_even(n)
elif not n%2 and int(n%4):
    l = singly_even(n)
    
t = time.time()

if not n == 2:
    printer(l)
else:
    print("There is no magic square for n=2")
print((t-t0)*1000, "ms")