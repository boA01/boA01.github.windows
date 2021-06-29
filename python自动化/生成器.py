# generator

#保存的是算法
# 是一种 Iterator(next), Iterable(for)

def f():
    l1 = (i for i in range(10))
    l2 = iter([i for i in range(10)])

def fib(max):
    n, a, b = 0, 1, 0
    while n<max:
        yield b
        a, b = b, a+b
        n+=1
    return "done"

def yanghuisanjiao():
    l = [1]
    while 1:
        i=1
        temp = l[:]
        while i<len(l):
            l[i]=temp[i-1]+temp[i]
            i+=1
        yield(l[:])
        l.append(0)

if __name__ == "__main__":
    # for i in fib(8):
        # print(i)
    yh = yanghuisanjiao()
    for i in range(3):
        print(next(yh))

