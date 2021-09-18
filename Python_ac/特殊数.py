while 1:
    try:
        for n in range(100,1000):
            b = n//100
            s = n//10%10
            g = n%10
            if b**3+s**3+g**3 == n:
                print(n)
        break
    except:
        break