# https://www.acmicpc.net/problem/10870

a = 0; b = 1
n = int(input())
while n > 0:
    n -= 1

    c = a + b
    a = b
    b = c

print(a)