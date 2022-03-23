import pandas as pd
import numpy as np
from math import sqrt, hypot, floor, ceil
R = 5

# 构造数据
def reset():
    x = np.random.normal(25, 8, 400).astype(int)
    y, z = np.random.randint(0, 51, (2, 400))
    df = pd.DataFrame(data = {
        "x":x,
        "y":y,
        "z":z
    })
    df = df.sort_values(by = 'x', ascending = False)
    df.to_csv(r"data.csv", index = False)

# 读取结点信息
df = pd.read_csv(r"data.csv")

# 读取栅栏数据
def read_zl_x(x):
    if x-R < 0:
        df_x = df.loc[(df['x'] >= 0) & (df['x'] < x+R)]
    elif x+R > 50:
        df_x = df.loc[(df['x'] > x-R) & (df['x'] <= 50)]
    else:
        df_x = df.loc[(df['x'] > x-R) & (df['x'] < x+R)]
    return df_x

# 取整
def qz(num):
    if num < 0:
        return 0
    elif num > 100:
        return 100
    return num

# 正向标记
def jd_append(arr_100, Y, Z, r):
    y1, z1 = qz(floor(Y-r)), qz(floor(Z-r))
    y2, z2 = qz(ceil(Y+r)), qz(ceil(Z+r))
    res = 0
    for z in range(z1, z2):
        zz = abs(Z-z)
        for y in range(y1, y2):
            if hypot(abs(Y-y), zz) <= r:
                arr_100[y, z] += 1 # 上色
                if arr_100[y, z] == 1: # 唯一标记
                    res += 1
    return res

# 反向清除
def jd_remove(arr_100, Y, Z, r):
    y1, z1 = qz(floor(Y-r)), qz(floor(Z-r))
    y2, z2 = qz(ceil(Y+r)), qz(ceil(Z+r))
    for z in range(z1, z2):
        zz = abs(Z-z)
        for y in range(y1, y2):
            if hypot(abs(Y-y), zz) <= r:
                if arr_100[y, z] == 1: # 存在唯一标记
                    return True
    for z in range(z1, z2):
        zz = abs(Z-z)
        for y in range(y1, y2):
            if hypot(abs(Y-y), zz) <= r:
                arr_100[y, z] -= 1 # 去色
    return False

# 切面覆盖优化
def cover(i, df_x):
    arr_100 = np.zeros([100, 100], dtype=int)
    arr = df_x.values
    px, r1 = 0, 0
    arr_y = []

    for x, y, z in sorted(arr, key= lambda a:abs(a[0]-i)):
        if px != x:
            px = x
            l = abs(x-i)
            r = sqrt(R**2-l**2)
        if tmp := jd_append(arr_100, y*2, z*2, r*2): # 存在唯一标记的结点
            r1 += tmp
            # 添加结点
            arr_y.append([x, y, z])

    for x, y, z in arr_y[::-1]:
        if px != x:
            px = x
            l = abs(x-i)
            r = sqrt(R**2-l**2)
        if not jd_remove(arr_100, y*2, z*2, r*2): # 不存在唯一标记
            # 去除冗余结点
            arr_y.remove([x, y, z])

    return pd.DataFrame([[i, round(r1/10000, 3), len(df_x), len(arr_y)]], columns=['x', 'f', 'n1', 'n2'])

# 栅栏面结点
def cover_jd(i):
    arr_100 = np.zeros([100, 100], dtype=int)
    arr = read_zl_x(i).values
    px, r1 = 0, 0
    arr_y = []

    for x, y, z in sorted(arr, key= lambda a:abs(a[0]-i)):
        if px != x:
            px = x
            l = abs(x-i)
            r = sqrt(R**2-l**2)
        if tmp := jd_append(arr_100, y*2, z*2, r*2): # 存在唯一标记的结点
            r1 += tmp
            # 添加结点
            arr_y.append([x, y, z])

    for x, y, z in arr_y[::-1]:
        if px != x:
            px = x
            l = abs(x-i)
            r = sqrt(R**2-l**2)
        if not jd_remove(arr_100, y*2, z*2, r*2): # 不存在唯一标记
            # 去除冗余结点
            arr_y.remove([x, y, z])

    return round(r1/100, 3), arr_y

def main():
    df_x = pd.DataFrame(columns=['x'])
    for i in range(51):
        df_x = pd.concat([df_x, cover(i, read_zl_x(i))])
    df_x.to_csv(r"data1.csv", index=False)

if __name__ == "__main__":
    main()
