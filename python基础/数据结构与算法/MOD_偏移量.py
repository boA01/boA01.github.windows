'''
小明同学需要对一个长度为 N 的字符串进行处理，他需要按照要求
执行若干步骤，每个步骤都均为下面 2 种操作中的一种，2 种操作如下：
TYPE 1. 从字符串结尾开始算起，将第 X 个字符之前的字符移动到字符串末尾
TYPE 2. 输出字符串索引为 X 的字符

6 2
xiaomi
1 2 mixiao
2 0 m

m
'''

N, T = map(int, input().split())
s = input()
cur = 0

for i in range(T):
    Type, X = map(int, input().split())
    if Type == 1:
        cur += N-X
        cur %= N
    else:
        print(s[(cur+X)%N])