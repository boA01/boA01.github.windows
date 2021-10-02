a=[1,2,3,8,6,7,5,10,16,98,99,100,101]

s = []
n = 1

for i in range(1,len(a)):
    if a[i]==a[i-1]+1:
        n+=1
    else:
        s.append(n)
        n = 1
s.append(n)

print(max(s))