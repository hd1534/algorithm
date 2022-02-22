# https://www.acmicpc.net/problem/15652


def dfs(n, m, arr):
    if m == 0:
        print(*arr)
        return

    start = arr[-1] if len(arr) else 1
    for i in range(start, n+1):
        dfs(n, m-1, arr+[i])


dfs(*map(int, input().split()), [])
