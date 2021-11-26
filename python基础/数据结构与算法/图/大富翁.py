M = 5 # 本钱
arr = [5,10,2,5] # 路线

n = len(reward)
dp = [0]*(n + 1)
dp[0] = M # 本金(0表示游戏还未开始)

# 动态规划求解
gold = 0
for i in range(1, n + 1):
    if i - 1 >=0 and dp[i - 1] >= 2: # 可以走一格的情况下, 消耗2
        dp[i] = max(dp[i], dp[i - 1] + arr[i - 1] - 2) # 通过走一格的方式从i-1到i
    if i - 2 >= 0 and dp[i - 2] >= 3: # 可以跳一格的情况下，消耗3
        dp[i] = max(dp[i], dp[i - 2] + arr[i - 1] - 3) # 通过跳两格的方式从i-2到i
    gold = max(gold, dp[i])

print(gold) # 利益最大
print(dp)