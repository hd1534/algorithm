# https://www.acmicpc.net/problem/1018

def patternCheck(pattern: str, board: list, n: int, m: int) -> list:
    '''패턴과 맞지 않는 부분이 True인 배열 반환

    str에 "WB" 나 "BW"를 주면됨'''

    arr = [[None] * m for _ in range(n)]  # 패턴과 다른 곳 기록할 배열

    for i in range(n):
        for j in range(m):
            # 패턴이 줄마다 번갈아 가므로 i를 넣음
            arr[i][j] = (board[i][j] != pattern[(i+j) % 2])

    return arr


def findMin(arr: list, n: int, m: int) -> int:
    '''patternCheck에서 반환된 배열을 가지고 8*8 체스판으로 만들때 가장 적게 수정하는 횟수 반환'''

    result = float("inf")
    sumTable = [[None] * m for _ in range(n-7)]  # 8개씩 묶어두기

    # 밑으로 8개씩 더해둔 테이블 작성
    for i in range(n-7):
        for j in range(m):
            sumTable[i][j] = sum([arr[k][j] for k in range(i, i+8)])

    # 옆으로 8개씩 더하기
    for l in sumTable:
        for j in range(m-7):
            tmp = sum(l[j:j+8])
            if tmp < result:
                result = tmp

    return result


if __name__ == "__main__":
    n, m = map(int, input().split())
    board = [input() for _ in range(n)]
    print(min(findMin(patternCheck("WB", board, n, m), n, m),
          findMin(patternCheck("BW", board, n, m), n, m)))
