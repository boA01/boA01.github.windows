# 和最大子串
arr = [-2, 1, -3, 4, -1, 2, 1, 5, 4]
#     [-2, 1, -2, 4, 3, 5, 6, 11, 15]

l = len(arr)
dp = [0]*l
Max = dp[0] = arr[0]

for i in range(1, l):
    dp[i] = max(arr[i], dp[i-1]+arr[i]) # 是否另立门户
    if dp[i] > Max:
        Max = dp[i]

print(Max)
print(dp)