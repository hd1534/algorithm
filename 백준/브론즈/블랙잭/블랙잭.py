# https://www.acmicpc.net/problem/2798

def jack(arr):
    best = 0
    for i in range(len(arr)-2):
        for j in range(i+1, len(arr)-1):
            for k in range(j+1, len(arr)):
                sum = arr[i] + arr[j] + arr[k]
                if sum == m:
                    return sum
                elif best < sum < m:
                    best = sum

    return best


n, m = map(int, input().split())
arr = sorted(map(int, input().split()))


print(jack(arr))
