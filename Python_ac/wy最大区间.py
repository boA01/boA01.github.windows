'''
给定一个数组序列, 需要求选出一个区间, 使得该区间
是所有区间中经过如下计算的值最大的一个：区间中的
最小数 * 区间所有数的和最后程序输出经过计算后的最
大值即可，不需要输出具体的区间。如给定序列  [6 2 1]
则根据上述公式, 可得到所有可以选定各个区间的计算值:


[6] = 6 * 6 = 36;
[2] = 2 * 2 = 4;
[1] = 1 * 1 = 1;
[6,2] = 2 * 8 = 16;
[2,1] = 1 * 3 = 3;
[6, 2, 1] = 1 * 9 = 9;
'''

# 遍历每个数，并找出该数的最大区间，即该数在区间中最小，加总求积
if __name__ == "__main__":
    n = int(input())
    inlist = list(map(int,input().split()))
 
    res = 0
    for i in range(n):
        tmp = inlist[i]
        if tmp == 0:
            continue
        l = r = i
        while l - 1 >= 0 and inlist[l - 1] >= tmp:
            l -= 1
        while r + 1 < n and inlist[r + 1] >= tmp:
            r += 1
        res = max(res, tmp * sum(inlist[l:r + 1]))
    print(res)