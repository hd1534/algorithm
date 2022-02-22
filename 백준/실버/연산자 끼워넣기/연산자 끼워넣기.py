# https://www.acmicpc.net/problem/14888

func = [
    lambda x, y: x+y,
    lambda x, y: x-y,
    lambda x, y: x*y,
    lambda x, y: int(x/y),
]

maximum = -float('inf')  # 최대값이 음수일 때 생각 안하고 0으로 해두고서 왜 틀렸지 이러고 있었네 ㅋㅋㅋㅋㅋㅋㅋㅋ
minimum = float('inf')


def dfs(n: int, arr: list, operatorCount: list, result: int) -> None:
    global func, maximum, minimum

    if n == 1:
        maximum = max(maximum, result)
        minimum = min(minimum, result)
        return

    n -= 1
    for i in range(4):
        if operatorCount[i] > 0:
            operatorCount[i] -= 1
            dfs(n, arr, operatorCount, func[i](result, arr[-n]))
            operatorCount[i] += 1


n = int(input())
arr = list(map(int, input().split()))
dfs(n, arr, list(map(int, input().split())), arr[0])
print(maximum)
print(minimum)
