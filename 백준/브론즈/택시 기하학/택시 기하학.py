# https://www.acmicpc.net/problem/3053

# |x1-x2| + |y1-y2| 이거는 마름모 꼴의 그래프가 나온다.

from math import pi

n = int(input())
print("%06f"%(pi*n*n))
print("%06f"%((n**2)*2))