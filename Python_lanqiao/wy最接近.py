s=list(map(int,input().split(",")))
ls=[]
k=int(input())
x=int(input())

for i in range(len(s)):
  ls.append((i,s[i]-x))

ls.sort(key=lambda x:x[1])

for i in range(k-1):
    print(s[i],end=",")

print(s[k-1])