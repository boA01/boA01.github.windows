import functools as ft

n = int(input())
s = str(ft.reduce(lambda x,y:sum((x,y)), range(n)))
l=0
print(s)

for i in s[::-1]:
    if i=='0':
        l+=1
    else:break
print(l)