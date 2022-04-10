import pandas as pd
import numpy as np
from math import sqrt, hypot, floor, ceil

R = 5            # 感知半径
L = 50           # 覆盖范围
NUM = 400        # 结点数目
MATRIX = 100     # 矩阵大小
MS = MATRIX**2   # 矩阵面积
MR = MATRIX/L    # 标记比例
ML = 10          # 最大移动距离

# 读取文件
df = pd.read_csv(r"data.csv")

# 构造数据
def reset():
    x = np.random.normal(25, 8, L).astype(int)
    y, z = np.random.randint(0, L, (2, L))
    df = pd.DataFrame(data = {
        "x":x,
        "y":y,
        "z":z
    })
    df = df.sort_values(by = 'x', ascending = False)
    df.to_csv(r"data.csv", index = False)

# 读取栅栏数据
def read_zl_x(x):
    if x-R < 0:
        df_x = df.loc[(df['x'] >= 0) & (df['x'] < x+R)]
    elif x+R > L:
        df_x = df.loc[(df['x'] > x-R) & (df['x'] <= L)]
    else:
        df_x = df.loc[(df['x'] > x-R) & (df['x'] < x+R)]
    return df_x

# 边界处理
def qz(num):
    if num < 0:
        return 0
    elif num > MATRIX:
        return MATRIX
    return num

# 正向标记
def jd_append(arr_100, Y, Z, r):
    y1, z1 = qz(floor(Y-r)), qz(floor(Z-r))
    y2, z2 = qz(ceil(Y+r)), qz(ceil(Z+r))
    res, flag = 0, False
    for z in range(z1, z2):
        zz = abs(Z-z)
        for y in range(y1, y2):
            if hypot(abs(Y-y), zz) <= r:
                # 存在唯一标记
                if arr_100[y, z] == 0:
                    flag = True
                    break
        if flag:
            break
    else:
        return 0

    for z in range(z1, z2):
        zz = abs(Z-z)
        for y in range(y1, y2):
            if hypot(abs(Y-y), zz) <= r:
                # 上色
                arr_100[y, z] += 1
                # 唯一标记
                if arr_100[y, z] == 1:
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
                # 存在唯一标记
                if arr_100[y, z] == 1:
                    return True
    # 不存在唯一标记，是冗余结点
    for z in range(z1, z2):
        zz = abs(Z-z)
        for y in range(y1, y2):
            if hypot(abs(Y-y), zz) <= r:
                # 去色
                arr_100[y, z] -= 1 
    return False

# 优化
def optimize(i, df_x):
    arr_100 = np.zeros([MATRIX, MATRIX], dtype=int)
    arr = df_x.values
    px, r1 = 0, 0
    arr_y = []

    for x, y, z in sorted(arr, key= lambda a:abs(a[0]-i)):
        if px != x:
            px = x
            l = abs(x-i)
            r = sqrt(R**2-l**2)
        # 存在唯一标记的结点
        if tmp := jd_append(arr_100, y*MR, z*MR, r*MR):
            r1 += tmp
            # 添加结点
            arr_y.append([x, y, z])

    for x, y, z in arr_y[::-1]:
        if px != x:
            px = x
            l = abs(x-i)
            r = sqrt(R**2-l**2)
        # 不存在唯一标记    
        if not jd_remove(arr_100, y*MR, z*MR, r*MR): 
            # 去除冗余结点
            arr_y.remove([x, y, z])

    return r1/MS, arr_y

# 切面优化信息
def cover(i, df_x):
    rate, arr_y = optimize(i, df_x)
    return pd.DataFrame(
        [
            [
                i,
                round(rate, 4),
                len(df_x),
                len(arr_y),
            ],
        ], 
        columns = ['x', 'f', 'n1', 'n2']
    )

# 优化后栅栏面
def cover_jd(i, df_x):
    rate, arr_y = optimize(i, df_x)
    return round(rate*100, 2), arr_y

# 结点移动
def jd_move():
    pass

def main():
    df_x = pd.DataFrame(columns=['x'])
    for i in range(L):
        df_x = pd.concat([df_x, cover(i, read_zl_x(i))])
    df_x.to_csv(r"data1.csv", index=False)

if __name__ == "__main__":
    main()
