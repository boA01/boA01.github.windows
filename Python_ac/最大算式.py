a,b=(map(eval, input("+个数:"+"-个数:").split(" ")))
n=list(map(eval, input("输入数字：").split(" ")))
s=0
n.reverse()

for i in range(int(a)+1):
    s+=n[i]
for j in range(int(a)+1,len(n)):
    s-=n[j]
print(s)