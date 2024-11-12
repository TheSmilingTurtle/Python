while True:
    s = input("Enter things: ")

    l = [float(x.strip().replace(",", ".")) for x in s.split()]

    print(l)
    print(sum(l))based on