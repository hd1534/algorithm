# https://www.acmicpc.net/problem/11726

n = int(input())

dp = [None, 1, 2] + [None]* n

for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 10007

print(dp[n])
