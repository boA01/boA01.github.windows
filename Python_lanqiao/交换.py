s='oslxlucjsqmfbglzihhxtjwehboynx'
# s='abcbaa'
# n=20
# m=0
# l=list(s)
# ss=set(s)
# ojhllucssqmfhglzihxxtjwebboynx


'''
m = 20
s = list(s)

arr = {}
for i in range(0,len(s)):
    if s[i] not in arr:
        arr[s[i]] = []
    arr[s[i]].append(i)
print(arr)
Max = 0
for i in arr:
    if len(arr[i])>Max:
        for j in range (Max,len(arr[i])):
            Sum = 0
            for k in range(0,j+1):
                Sum += abs(arr[i][(j//2)]-arr[i][k]) - abs((0+j//2)-k)
            if Sum <= m:
                Max = max(Max,j+1)
print(Max)



for i in range(1,n+1): #最多，小优先
    if n>i: #交换次数
        for j in ss:
            if j*2 in s: #存在连续就不交换
                continue
            if s.count(j)>1: #有机会连续
                try:
                    o = s.index(j) #当前坐标
                    p = s.index(j,o+2)-1 #交换坐标
                    if p-o==i:
                        l[o],l[p]=l[p],l[o]
                        s="".join(l) #更新字符串
                        print(f"{j}：{i}")
                        n-=i
                except:
                    pass

for a in set(s):
    if a*2 in s:
        m+=1

print(m)
'''