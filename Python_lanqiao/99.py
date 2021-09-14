def fn_for():
    for i in range(10):
        for j in range(1,i+1):
            print(f"{i}*{j}={i*j}",end="\t")
        print()

def fn_while():
    i=1
    while i<10:
        j=1
        while j<=i:
            print(f"{i}*{j}={i*j}",end="\t")
            j+=1
        i+=1
        print()