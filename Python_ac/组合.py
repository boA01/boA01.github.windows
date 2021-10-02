arr = "123BCa"
N = 5

l = len(arr)
arr2 = []

if l == N:
    arr2.append(''.join(sorted(arr)))
else:
    for i in range(int('1'*N,2),int('1'*l,2)):
        if (s:=format(i,f'0{l}b')).count("1") == N:
            print(i,"-->",s)
            item = []
            for j in range(l):
                if s[j]=='1':
                    item.append(arr[j])
            arr2.append(''.join(item))
print(sorted(arr2))
