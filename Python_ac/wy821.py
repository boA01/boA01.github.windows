#1 请列举两类常见的软件开发模型并描述其特点。
'''
瀑布模型：通过结构化、顺序和线性方法来开发软件
敏捷开发：开发与运营分离；

DevOps：开发 运营 相结合，开发运维一体化，
支持软件开发中的持续集成 (CI Jenkins) 和持续部署 (CD)、自动测试和透明进程

后两：尽可能有效快速的交付最终产品
'''

#2 数组中两个元素和小于等于M的组合数
def fn2():
    arr = list(map(int, input().split(" ")))
    M = int(input())
    l = len(arr)
    n = 0

    for i in range(l-1):
        x = arr[i]
        for j in range(i+1,l):
            if M>=abs(x-arr[j]):
                n+=1
    print(n)

#3 每一层至多摆放两个商品，而且商品的总长度不能
# 比货架长度长（已知单个商品的长度都不会比货架长
def fn3():
    X = int(input())
    arr = sorted(list(map(int, input().split(" "))),reverse=True)
    n = 0

    while len(arr)>1:
        if X>=arr[0]+arr[-1]:
            arr.pop(0)
            arr.pop(-1)
        else:
            arr.pop(0)
        n+=1

    if len(arr)==1:
        n+=1
    print(n)

#4 摩尔斯电码解码
def fn4():
    d = dict(zip(
        ['0', '1', '10', '11', '100', '101', '110', '111'],
        ['A','B','C','D','E','F','G']
        ))

    while 0:
        s = input().split("0")
        for i in s:
            print(i)

#5 最长和谐连续子序列
def fn5():
    arr = list(map(int, input().split(' ')))
    l = len(arr)-1
    arr1 = [0]

    for i in range(l):
        m=i+1
        q = min(arr[i:i+2])
        n=0
        while m<l+1 and abs(q-arr[m])<=1:
                n+=1
                m+=1
        arr1.append(n)

    print(r if (r:=max(arr1))==0 else r+1)

#6 大富翁游戏
def fn6():
    M = int(input())
    reward = list(map(int, input().strip().split()))
    n = len(reward)
    dp = [0]*(n + 1)
    dp[0] = M       # 起始的本金(0表示游戏还未开始)
    # 动态规划求解
    gold = 0
    for i in range(1, n + 1):
        if i - 1 >=0 and dp[i - 1] >= 2:
            # 可以走一格的情况下
            dp[i] = max(dp[i], dp[i - 1] + reward[i - 1] - 2)     # 通过走一格的方式从i-1到i
        if i - 2 >= 0 and dp[i - 2] >= 3:
            # 可以跳一格的情况下
            dp[i] = max(dp[i], dp[i - 2] + reward[i - 1] - 3)     # 通过跳两格的方式从i-2到i
        gold = max(gold, dp[i])
    print(gold)
    '''
    m = int(input())
    arr = list(map(int,input().split(" ")))
    res = [m]

    for i in range(len(arr)-1):
        if (x:=m+arr[i]-2)>2: #走
            res.append(x)
            pass
        elif (x:=m+arr[i+1]-3)>3: #跳
            res.append(x)
            pass
    print(max(res))
    '''
# fn6()

# 他们围成一圈，年龄高的小孩要比临近他的小孩
# 多给纸张，求最少要给这些小孩多少纸张
def fn7():
    arr = list(map(int,input().split()))
    arr1 = sorted(set(arr))
    n = 1
    m = 0

    for i in arr1:
        m += arr.count(i)*n
        n+=1
    print(m)
# fn7()

# abcxyz
def fn8():          
    arr = input()
    s = ''
    arr1 = [0]

    for i in range(len(arr)):
        if (ii:=arr[i]) in s: # 之后的个数
            n = arr[i:].count(ii)
            if n>1 and n&1==0: # 偶数个
                arr1.append(arr.rindex(ii)+1-i)
            elif n>2: # 奇数个
                # print(ii, arr.rindex(ii))
                # print(arr[i:arr.rindex(ii)].rindex(ii))
                arr1.append(arr[i:arr.rindex(ii)].rindex(ii)+1-i)

    print(max(arr1))

# 0表示水，1表示陆地，2表示障碍物
# 走水路要花2钱，走陆地要花1钱，障碍物没法走
# 求从左上角，到右下角要花的最少的钱，如果走不过去，
# 那么就返回-1
def fn9():
    arr = [[1,1,1,1,0],[0,1,0,1,0],[1,1,2,1,1],[0,2,0,0,1]]
    for i in arr:
        try:
            print(arr[][1])
            # print(arr[0].index(0))
            # print(arr[][1].index(0))
        except:
            print("bc")

fn9()