# https://www.acmicpc.net/problem/1463

def nTo1(n: int) -> int:
    arr = [0, 0] + [float('inf')]*n

    for i in range(1, n):
        if i+1 <= n:
            arr[i+1] = min(arr[i+1], arr[i] + 1)
        if i*2 <= n:
            arr[i*2] = min(arr[i*2], arr[i] + 1)
        if i*3 <= n:
            arr[i*3] = min(arr[i*3], arr[i] + 1)

    return arr[n]


print(nTo1(int(input())))
