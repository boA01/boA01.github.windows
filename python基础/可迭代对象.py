# container(容器)->iterable(可迭代对象)
# generator(生成器<next()>)->iterator(迭代器<for>)->iterable(可迭代对象)--iter()->iterator(迭代器)


# 可迭代对象-列表
l1 = list(range(10))
print(type(l1))
print(l1)

# 可迭代对象-列表生成式
l2 = [i if i%2==0 else -i for i in range(10) if i%3!=0]
print(type(l2))
print(l2)


# iter(可迭代对象) -> 迭代器
l3 = iter(l1)
while 1:
    try:
        print(next(l3))
    except EOFError as identifier:
        # print(identifier)
        break

# 可迭代对象-迭代器-生成器-生成器表达式
l4 = (i for i in range(10))
print(type(l4))

# 可迭代对象-迭代器-生成器-生成器函数
def gen(n):
    while n>0:
        yield n
        n-=1

def gen1(n):
    yield from gen(n)


def gen2_1(l):
    for i in l:
        yield i

def gen2_2(l):
    yield from l