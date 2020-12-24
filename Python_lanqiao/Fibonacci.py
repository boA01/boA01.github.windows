# print([1,1,1,2,3,5,8,13,21,34,55])

n = int(input())

Fib = [1 for i in range(n+1)]

k = 3

while k<=n:
    
    Fib[k] = (Fib[k-1] + Fib[k-2]) % 10007

    k += 1

print(Fib[n])