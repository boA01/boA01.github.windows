s = input()
t = []
 
for i in s:
    if i in '"[]()':
        t.append(i)

if (l:=len(t))&1==0 and l>0:
    h = l>>1
    if t[:h]==t[:h-1:-1]:
        print('true')
    else:
        print('false')
else :
    print('false')