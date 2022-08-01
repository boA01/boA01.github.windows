import pandas as pd
import numpy as np
from math import sqrt, hypot, floor, ceil

R = 5            # 感知半径
L = 50           # 覆盖范围
NUM = 300        # 结点数目
MATRIX = 100     # 矩阵大小
MS = MATRIX**2   # 矩阵面积
MR = MATRIX/L    # 标记比例
ML = 10          # 最大移动距离
Arr_1 = np.ones(MATRIX, dtype=int) # 非零列

# 读取文件
df = pd.read_csv(r"data.csv")

# 构造数据
def reset():
    # 正太分布
    x = np.random.normal(25, 8, NUM).astype(int)
    # 随机分布
    y = np.random.randint(0, L, NUM)
    # 零值
    z = np.random.randint(0, L, NUM)
    # z = np.zeros(NUM, dtype = int)
    df = pd.DataFrame(data = {
        "x":x,
        "y":y,
        "z":z
    })
    df = df.sort_values(by = 'x', ascending = False)
    df.to_csv(r"data.csv", index = False)

# 读取栅栏数据(x-R < x < x+R)
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
    elif (m:=MATRIX-1) < num:
        return m
    return int(num)

# 结点分类(x==n)
def sort_y(df_xy):
    return df_xy.sort_values(by = 'y', ascending = False).values

# 标记
def mark(arr_100, Y, Z, r):
    y1, z1 = qz(floor(Y-r)), qz(floor(Z-r))
    y2, z2 = qz(ceil(Y+r)), qz(ceil(Z+r))
    res = 0

    for z in range(z1, z2):
        zz = abs(Z-z)
        for y in range(y1, y2):
            if hypot(abs(Y-y), zz) <= r:
                # 上色
                arr_100[z, y] += 1
                # 唯一标记
                if arr_100[z, y] == 1:
                    res += 1
    return res

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

# 优化-随机部署去冗余
def optimize(i, df_x):
    arr_100 = np.zeros([MATRIX, MATRIX], dtype=int)
    arr = df_x.values
    px, r1 = 0, 0
    arr_y = []

    for x, y, z in sorted(arr, key = lambda a:abs(a[0]-i)):
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

# 优化后栅栏面
def cover_jd(i, df_x):
    rate, arr_y = optimize(i, df_x)
    return round(rate*100, 2), arr_y

# 获取高度
def h_z(h, arr_l, arr_r):
    # 快慢指针
    s = 0
    for f in range(MATRIX):
        if arr_l[f] != 0 or arr_r[f] != 0:
            s = f
        else:
            if (tmp:=(f-s)>>1) >= h:
                return s+tmp
    return 0

# 结点移动-双探测线
def jd_move(i, df_x):
    arr_100 = np.zeros([MATRIX, MATRIX], dtype=int)
    arr = []
    mk = 0
    for d in range(R):
        # 相同距离结点
        arr_d = sort_y(df_x.loc[df_x["x"].isin([i-d, i+d])])
        # # 切面圆半径
        r = sqrt(R**2-d**2)
        '''
        5/sqrt(2) ~= 3.5 - 0.5 ~= 3
        4/sqrt(2) ~= 2.8 - 0.5 ~= 2
        3/sqrt(2) ~= 2.1 - 0.5 ~= 1
        '''
        # 距离法线长度
        dr = floor(r/sqrt(2)-0.5)
        for x, y, _ in arr_d:
            # 左探测线
            r_l = qz((y-dr)*MR)
            # 右探测线
            r_r = qz((y+dr)*MR)
            # print(f"{x=}, {r_l}, {r_r}")
            # 高度
            z = h_z(dr, arr_100[:, r_l], arr_100[:, r_r])
            # print(, {y=}, {z=}")
            if z == 0:
                continue
            # 标记个数
            tmp = mark(arr_100, y*MR, z, r*MR)
            if tmp:
                mk += tmp
                # 添加结点
                arr.append([x, y, z//MR])
    return round(mk/MS, 4), arr

# 获取高度
def h_z1(h, arr, arr_l, arr_r):
    # h2 = h*2
    # 快慢指针
    s = 0
    for f in range(MATRIX):
        if (
            (arr_l[f] != 0 and arr[f] != 0) or 
            (arr[f] != 0 and arr_r[f] != 0) or 
            (arr_l[f] != 0 and arr_r[f] != 0)
        ):
            s = f
        else:
            if f-s >= h:
                return f
    return 0

# 结点移动--三探测线
def jd_move1(i, df_x):
    arr_100 = np.zeros([MATRIX, MATRIX], dtype=int)
    arr = []
    mk = 0
    for d in range(R):
        # 相同距离结点
        arr_d = sort_y(df_x.loc[df_x["x"].isin([i-d, i+d])])
        # 切面圆半径
        r = sqrt(R**2-d**2)
        # 探测线间距
        dr = r*sqrt(2)/2
        for x, y, _ in arr_d:
            # 中探测线
            c_l = qz(y*MR)
            # 左探测线
            l_l = qz((y-dr)*MR)
            # 右探测线
            r_l = qz((y+dr)*MR)
            if l_l == c_l:
                arr_l = Arr_1
            else:
                arr_l = arr_100[:, l_l]
            if r_l == y:
                arr_r = Arr_1
            else:
                arr_r = arr_100[:, r_l]
            # 高度
            z = h_z1(dr*MR, arr_100[:, c_l], arr_l, arr_r)
            if z == 0:
                continue
            # 标记个数
            tmp = mark(arr_100, y*MR, z, r*MR)
            if tmp:
                mk += tmp
                # 添加结点
                arr.append([x, y, z//MR])
    return round(mk/MS, 4), arr

# 切面优化信息
def cover(i, df_x):
    # rate, arr_y = optimize(i, df_x)
    # rate, arr_y = jd_move(i, df_x)
    rate, arr_y = jd_move1(i, df_x)
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

def main():
    df_x = pd.DataFrame(columns=['x'])
    for i in range(L):
        df_x = pd.concat([df_x, cover(i, read_zl_x(i))])
    df_x.to_csv(r"db1.csv", index=False)
    # df_x.to_excel(r"fz3.xls", index=False)

if __name__ == "__main__":
    reset()
    # main()
    # print(jd_move1(6, read_zl_x(6)))
