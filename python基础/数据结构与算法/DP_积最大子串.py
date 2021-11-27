# 积最大子串
arr = [2,3,-2,0,4,-2,-2,-3,5]
# dp  [2,6,-2,0,4,-2,2,48,240]
#     [2,6,-12,0,4,-8,16,-48,30]

l = len(arr)
dp = [0]*l
dp[0]=arr[0]
Max = 1

def f()
    for i in range(1, l):
        r = dp[i-1]*arr[i]
        dp[i]= arr[i] if arr[i] > abs(r) else r
        Max=max(Max, dp[i])

print(Max)
print(dp)