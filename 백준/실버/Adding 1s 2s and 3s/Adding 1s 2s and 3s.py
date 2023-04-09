# https://www.acmicpc.net/problem/9095

MAX_LEN = 11

dp = [0, 1, 1, 1] + [0] * MAX_LEN


for i in range(MAX_LEN):
    dp[i+1] += dp[i]
    dp[i+2] += dp[i]
    dp[i+3] += dp[i]


for _ in range(int(input())):
    n = int(input())
    
    print(dp[n])
