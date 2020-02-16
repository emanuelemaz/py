def scomposizione(n):
    d = 2
    f = (str(n) + "=1") 

    while int(n) >=d:
        if int(n) % d == 0:
            f = f + '*' + str(d)
            n = int(n) / d
        else:
            d = d + 1

    print(str(f))