# https://www.acmicpc.net/problem/7568

def findRanking(arr: list, x: int, y: int) -> int:
    ranking = 1
    for p, q in arr:
        if p > x and q > y:
            ranking += 1

    return ranking


arr = [list(map(int, input().split())) for _ in range(int(input()))]
print(" ".join([str(findRanking(arr, x, y)) for x, y in arr]))
