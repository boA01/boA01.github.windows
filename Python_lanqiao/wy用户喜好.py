'''
5
1 2 3 3 5
3
1 2 1
2 4 5
3 5 3

1
0
2

样例解释:
有5个用户，喜好值为分别为1、2、3、3、5，
第一组询问对于标号[1,2]的用户喜好值为1的用户的个数是1
第二组询问对于标号[2,4]的用户喜好值为5的用户的个数是0
第三组询问对于标号[3,5]的用户喜好值为3的用户的个数是2
'''
import copy

# n = int(input())
habby = map(int,input().split(" "))
# m = int(input())
arr = [[1, 2, 1],[2, 4, 5],[3, 5, 3]]
'''
for i in range(m):
    arr.append(list(map(int,input().split(" "))))

for j in arr:
    a,b,c=j
    print(habby[a-1:b].count(c))
'''

# for i in range(m):
#     arr.append(list(map(int,input().split(" "))))

def fn(a, b, c, hab):
    num = 0
    for k in range(b):
        try:
            o = next(hab)
            if c==o and k>=a:
                num+=1
        except:
            break
    return num

for j in arr:
    a,b,c=j
    num=0
    hab = copy.deepcopy(habby)
    print(fn(a-1, b, c, hab))
    