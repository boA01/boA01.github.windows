# n = int(input(":"))

# 十进制转其他进制
print(bin(64)[2:])
print(oct(64)[2:])
print(hex(188)[2:].upper())
format(177, "0b")

# 其他进制转十进制 int(str,base=10)
print(int("1000", 2))
print(int("12", 8))
print(int("f", 16))
print(int('11', 6))

# 转换函数
def n2N(n=4, arr='0123'):
    l = len(arr)
    arr1 = []

    while n>0:
        arr1.append(arr[n%l])
        n = n//l

    return ''.join(arr1.reverse())