import math
import time
m_s = []
c = 0
sum_s = 0
t3 = 0

def magic_square_3(a):
    n1 = int(input("Choose a number "))
    n2 = int(input("Choose another number "))
    n3 = int(input("Choose another number "))
    m_s[0][0]= n3-n2
    m_s[0][1]= n3+n1+n2
    m_s[0][2]= n3-n1
    m_s[1][0]= n3-n1+n2
    m_s[1][1]= n3
    m_s[1][2]= n3+n1-n2
    m_s[2][0]= n3+n1
    m_s[2][1]= n3-n1-n2
    m_s[2][2]= n3+n2
    return a

def magic_square_multiple_4(a):
    m_s2 = []
    b = 0
    e = int(math.pow(a, 2))
    f = int(a/4)
    g = 0
    while b < a:
       m_s2.append([])
       d = 0
       while d < a:
           m_s2[b].append(e)
           d += 1
           e -= 1
       b += 1
    for x in range (0, f):
        for y in range (0, f):
            m_s[g*x][g*y+1] = m_s2[g*x][g*y+1]
            m_s[g*x][g*y+2] = m_s2[g*x][g*y+2]
            m_s[g*x+1][g*y] = m_s2[g*x+1][g*y]
            m_s[g*x+1][g*y+3] = m_s2[g*x+1][g*y+3]
            m_s[g*x+2][g*y] = m_s2[g*x+2][g*y]
            m_s[g*x+2][g*y+3] = m_s2[g*x+2][g*y+3]
            m_s[g*x+3][g*y+1] = m_s2[g*x+3][g*y+1]
            m_s[g*x+3][g*y+2] = m_s2[g*x+3][g*y+2]
    return a

def magic_square_odd(a):
    b = 1
    g = a
    h = a*(a-1)
    for x in range(int(a/2), g):
        f = 0
        while f < a:
            m_s[f][x] = b
            if f == a-1:
                b = m_s[0][x]+a+2
            elif m_s[f][x] > h:
                b -= h-1
            elif not m_s[f][x]%a:
                b += 1
            else:
                b += a+1
            f += 1
    b = m_s[0][a-1]+2
    for x in range(0, int(a/2)):
        f = 0
        while f < a:
            m_s[f][x] = b
            if f == a-1:
                b = m_s[0][x]+a+2
            elif m_s[f][x] > h:
                b -= h-1
            elif not m_s[f][x]%a:
                b += 1
            else:
                b += a+1
            f += 1 
    return a

def magic_square_basic(a):
    b = 0
    e = 1
    while b < a:
        m_s.append([])
        d = 0
        while d < a:
            m_s[b].append(e)
            d += 1
            e += 1
        b += 1
    return a
    

def magic_square(t1, t3):
    a = int(input("How many numbers per side? (3, multiple of 4 or odd number) "))
    if not a or not a > 2:
        print("This is not what I said!!! You'll get a magic square of 3x3")
        a = 3
    t2 = time.time()
    t3 += t2-t1
    if not a%4:
        a = magic_square_basic(a)
        a = magic_square_multiple_4(a)
        return a, t3

    elif a == 3:
        a = magic_square_basic(a)
        a = magic_square_3(a)
        return a, t3
    
    elif a%2:
        a = magic_square_basic(a)
        a = magic_square_odd(a)
        return a, t3

    else:
        print("This is not what I said!!!")
        return True, t3

t0 = time.time()
        
while True:
    t1 = time.time()
    a, t3 = magic_square(t1, t3)
    if a == True:
        a = magic_square(t1, t3)
    else:
        break
print("Magic Square %sx%s:" % (a,a))
while c < a:
    print(m_s[c])
    sum_s += m_s[0][c]
    c += 1
t4 = time.time()
t = t4-t0-t3
print("The sum of each side is:", sum_s)
print("It took %s ms" % (t*1000))

