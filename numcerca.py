def numcerca(d):


    n = d - 1
    while d % n != 0:
        n -= 1
        if d % n == 0:
            print(n)
            dec = input("Vuoi continuare? (y/n)")
            if dec == "y":
                while (d - 1) % n != 0:
                    n -= 1
                    if d % n == 0:
                        print(n)
                        dec = input("Vuoi continuare? (y/n)")
            else:
                break