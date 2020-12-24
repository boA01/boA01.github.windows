while 1:
    try:
        n=sorted(list(map(eval, input("numbs:").split(" "))))
        print(n)
    except:
        break