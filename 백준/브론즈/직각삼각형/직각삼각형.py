# https://www.acmicpc.net/problem/4153

while True:
    arr = sorted(map(int, input().split()))
    if arr[0] == 0: break

    print("right" if arr[2]**2 == arr[0]**2 + arr[1]**2 else "wrong")
