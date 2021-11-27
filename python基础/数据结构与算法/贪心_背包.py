arr = [
    [1, 10, 60], # 数量，货重，单价
    [2, 30, 100],
    [3, 30, 130]
]
n = 50 # 限重
M = 0 # 总价

def f(n, M, arr):
    while n>0:
        for i in sorted(arr, key=lambda x:x[2]/x[1], reverse=True): # 性价比优先
            print(i)
            if x:=n//i[1]: # 需求量
                if x <= i[0]: # 需求量<=供应量
                    print(i, x)
                    M+=x*i[2]
                    n-=x*i[1]
                else: # 需求量>供应量
                    print(i, i[0])
                    M+=i[0]*i[2]
                    n-=i[0]*i[1]
            elif i[1]>n:
                return M

print(f(n, M, arr))