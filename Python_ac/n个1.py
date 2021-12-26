n = int(input())
m = 0

for i in range(1<<(n-1), 1<<n):
    s = format(i, "0b")
    if '00' not in s:
        m+=1
print(m)