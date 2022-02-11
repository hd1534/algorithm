# https://www.acmicpc.net/problem/15650


def dfs(start, n, m, arr):
    if m == 0:
        print(" ".join(map(str, arr)))
        return

    for i in range(start, n+1):
        dfs(i+1, n, m-1, arr+[i])


if __name__ == "__main__":
    n, m = map(int, input().split())

    dfs(1, n, m, [])
