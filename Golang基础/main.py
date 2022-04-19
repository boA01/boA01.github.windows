import itertools as it 

# n = int(input())
# arr = []
# for _ in range(n):
#     a = list(map(int, input().split(" ")))
#     arr.append(a)

# s = set()
# for i in it.product(*arr): # 笛卡尔积
#     s.add(sum(i)) # 集合去重
# print(len(s))


# strList, flag, arr = input(), 0, []
# for i in range(len(strList)):
#     if strList[i] == "(":
#         flag+=1
#     elif flag:
#         if strList[i] == ")":
#             flag-=1
#     elif strList[i] == "<":
#         arr.pop()
#     else:
#         arr.append(strList[i])
# print("".join(arr))


# def test():
#     n = int(input())
#     arr = list(map(int, input().split(" ")))

#     dp = [0 for _ in range(n)]
#     maxH = arr[0]
#     for i in range(len(arr)):
#         if i <= maxH:
#             dp[i] = i+arr[i]
#             maxH = max(dp[i], maxH)
#         else:
#             return 0
#     return 1

# print(test())


# def fun():
#     arr = list(map(int, input().split(" ")))
#     s = sum(arr) # 盲盒总价值
#     for i in range(s//max(arr), 1, -1):
#         if s%i == 0:
#             tmp = s//i # 单个盲盒价值
#             print(tmp, i)
#             arrtmp = arr # cpoy一份
#             while leng := len(arrtmp):
#                 for j in range(1, 1<<leng):
#                     b = format(j, f"0{leng}b") # 二进制表示组合种类（精华！！！）
#                     if sum(it.compress(arrtmp, map(int, b))) == tmp: # 满足价值的礼物组合
#                         # 剩下的礼物
#                         arrtmp = [arrtmp[i] for i in range(len(b)) if b[i] == '0']
#                         break
#                 else:
#                     break
#             if len(arrtmp) == 0: # 礼物全部放入盲盒
#                 return i
#     return 1

# print(fun())

# def yh():
#     str_ = input()
#     leng = len(str_)
#     idx = 0
#     if leng < 2:
#         return "NO"
#     while idx < leng:
#         if (tmp := str_[idx:idx+2]) == "ci" or tmp == "ti":
#             idx+=2
#             continue
#         elif str_[idx:idx+4] == "bank":
#             idx+=4
#             continue
#         return "NO"
#     return "YES"

# print(yh())

# n = int(input())

# for i in range(n//5):
#     for j in range(n//3):
#         temp = n - i - j
#         if 5 * i + 3 * j + temp / 3 == n and temp % 3 == 0:
#             print(i, j, temp)

# n = int(input())
# count = 0

# for i in range(n//10+1):
#     for j in range(n//5+1):
#         for k in range(n//2+1):
#             for l in range(n+1):
#                 if i*10+j*5+k*2+l == n:
#                     count+=1
# print(count)

# nums = [10, 9, 2, 5, 3, 6, 101, 18]
# res = 1
# leng = len(nums)
# dp = [1 for _ in range(leng)]

# for i in range(1, leng):
#     for j in range(i):
#         if nums[i] > nums[j]:
#             tmp = dp[j] + 1
#             if dp[i] < tmp:
#                 dp[i] = tmp
#     if res < dp[i]:
#         res = dp[i]
# print(res)

# 减法
def jf(lb, bjs, js):
    # 商
    count = 0
    # 高位游标
    cur = 0
    while cur<lb and bjs[cur] >= js[cur]:
        for i in range(len(bjs)-1, -1, -1):
            tmp = int(bjs[i]) - int(js[i])
            # print(bjs, i, tmp)
            # 借位
            if tmp < 0:
                bjs[i] = str(int(bjs[i])+10 - int(js[i]))
                for j in range(i-1, cur-1, -1):
                    if bjs[j]=='0':
                        bjs[j]='9'
                    else:
                        bjs[j]=str(int(bjs[j])-1)
                        break
                else:
                    return 0, bjs
            else:
                bjs[i] = str(tmp)
            count+=1
        # 高位右边右移
        if bjs[cur] == '0':
            cur+=1
    while bjs[0] == '0':
        bjs.pop(0)
        # 整除
        if not bjs:
            return count, ['0']
    return count, bjs

# print(jf(['1'], '5'))

bs = input()
cs = input()
lb = len(bs)
lc = len(cs)
l = 0
s = []
for v in range(lb):
    s.append(bs[v])
    if s[0] < cs[0]:
        if len(s) > lc:
            print(s, '0'+cs)
            _, s = jf(lb, s, '0'+cs)
    else:
        if len(s) == lc:
            print(s, cs)
            _, s = jf(lb, s, cs)
print(s)

# 统计数字
# def count_num(s):
#     count, cur, leng = 0, 0, len(s)

#     while cur < leng:
#         if '0' <= s[cur] <= '9':
#             count+=1
#             while cur < leng and '0' <= s[cur] <= '9':
#                 cur+=1
#         cur+=1
#     return count

# print(count_num("a00"))


# import os

# def test(file, str, new_str):
#     with open(file, "r", encoding="utf-8") as f1, open("%s.bak" % file, "w", encoding="utf-8") as f2:
#         for lin in f1:
#             for old_s in str:
#                 lin = lin.replace(old_s, new_str)
#             f2.write(lin)
#     os.remove(file)
#     os.rename("%s.bak" % file, file)


# old_str = ''
# with open("hello.txt", "r", encoding="utf-8") as f:
#     old_str = f.split()

# test("world.txt", old_str, "xxx")