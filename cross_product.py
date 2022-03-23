res = [None,None,None]

Anum = input("v1: ")
Bnum = input("v2: ")

a = Anum.split(",")
b = Bnum.split(",")

res[0] = int(a[1])*int(b[2])-int(a[2])*int(b[1])
res[1] = int(a[2])*int(b[0])-int(a[0])*int(b[2])
res[2] = int(a[0])*int(b[1])-int(a[1])*int(b[0])

print("The cross product is: \n",res[0],",",res[1],",",res[2])