# https://www.acmicpc.net/problem/2231

def digitSum(n: int) -> int:
    return n + sum(map(int, str(n)))


def findGenerator(n: int) -> int:
    for i in range(10 ** max(0, len(str(n))-2), n):
        if n == digitSum(i):
            return i

    return 0


print(findGenerator(int(input())))
