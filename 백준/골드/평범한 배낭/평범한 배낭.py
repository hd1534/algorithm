# https://www.acmicpc.net/problem/12865


n, k = map(int, input().split())
dp = {0: 0}  # {w: v}

for _ in range(n):
    w, v = map(int, input().split())
    for dp_w, dp_v in list(dp.items()):
        if (t := w + dp_w) > k:
            continue

        dp[t] = max(dp_v + v, dp.get(t, 0))

print(max(dp.values()))
