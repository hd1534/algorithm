# https://www.acmicpc.net/problem/11399


sum = 0
n = int(input())
for i in sorted(map(int, input().split())):
    sum += i * n
    n -= 1

print(sum)
