import functools as ft
a=[1,2,3,8,6,7,5,10,16,98,99,100,101]

s=[]
for i in range(1, len(a)):
    if (n:=a[i-1])==a[i]-1:
        s.append(n)
    else:
        s.append("n")
print(s)