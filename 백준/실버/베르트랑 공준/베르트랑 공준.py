# https://www.acmicpc.net/problem/4948

def createPrimeNumberTable(n: int) -> list:
    '''n크기의 소수 테이블, 1이면 소수'''
    arr = [0, 0] + [1] * n

    i = 2
    while i < len(arr):
        if arr[i] == 1:
            j = i+i
            while j < len(arr):
                arr[j] = 0
                j+=i
        i+=1

    return arr


if __name__ == "__main__":
    primeNumberTable = createPrimeNumberTable(123456*2)
    while True:
        n = int(input())
        if n == 0: break
        print(sum(primeNumberTable[n+1:2*n+1]))
