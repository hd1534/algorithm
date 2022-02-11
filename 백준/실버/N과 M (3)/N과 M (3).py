# https://www.acmicpc.net/problem/15651


n, m = map(int, input().split())
a = "1234567"
r = range(1, m+1)
exec("print('\\n'.join(["+"+' '+".join("i"*j for j in r) +
     "".join(" for "+"i"*i+" in a[:n]" for i in r)+"]))")
