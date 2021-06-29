# 可迭代对象 列表
l1 = list(range(10))
print(type(l1))
print(l1)

# 可迭代对象 列表生成式
l2 = [i if i%2==0 else -i for i in range(10) if i%3!=0]
print(type(l2))
print(l2)

# 迭代器 列表_生成器
l3 = (i for i in range(10))
print(type(l3))

while 1:
    try:
        print(next(l3))
    except EOFError as identifier:
        # print(identifier)
        break

# 迭代器
# iter 可迭代对象 -> 迭代器
l4 = iter(l1)

# yeild -> 迭代器

