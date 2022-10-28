# https://www.acmicpc.net/problem/1931

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x: list(reversed(x)))

tail = 0
count = 0
for s, e in arr:
    if s < tail:
        continue

    tail = e
    count += 1

print(count)
