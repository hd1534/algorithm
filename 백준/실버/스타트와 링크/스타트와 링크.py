# https://www.acmicpc.net/problem/14889

from itertools import combinations


def sumColumnAndRow(arr: list[int], i: int, j: int) -> int:

    return sum(arr[i]) + sum([a[j] for a in arr])


if __name__ == '__main__':
    n = int(input())
    halfOfN = n // 2
    arr = [list(map(int, input().split())) for _ in range(n)]

    sumOfArr = sum(map(sum, arr))
    sumOfColumnAndRows = [sumColumnAndRow(arr, i, i) for i in range(n)]

    answer = float('inf')
    for sums in combinations(sumOfColumnAndRows, halfOfN):
        answer = min(answer, abs(sumOfArr - sum(sums)))

    print(answer)


# # 기본적인 백트랙킹 알고리즘
# # pypy만 되고 python은 시간초과
# n = int(input())
# halfOfN = n // 2

# arr = [list(map(int, input().split())) for i in range(n)]

# answer = float('inf')

# isTeamA = [False for i in range(n)]


# def dfs(depth, countOfTeamA):
#     global n, halfOfN, arr, answer, isTeamA

#     if countOfTeamA == halfOfN:
#         tmp = 0

#         for i in range(n):
#             for j in range(n):
#                 if isTeamA[i] and isTeamA[j]:
#                     tmp += arr[i][j]
#                 elif not isTeamA[i] and not isTeamA[j]:
#                     tmp -= arr[i][j]

#         answer = min(answer, abs(tmp))
#         return

#     if (halfOfN - countOfTeamA) == (n - depth):
#         for i in range(depth, n):
#             isTeamA[i] = True

#         dfs(n, halfOfN)

#         for i in range(depth, n):
#             isTeamA[i] = False

#         return

#     isTeamA[depth] = True
#     dfs(depth + 1, countOfTeamA + 1)

#     isTeamA[depth] = False
#     dfs(depth + 1, countOfTeamA)


# if __name__ == '__main__':
#     dfs(0, 0)

#     print(answer)
