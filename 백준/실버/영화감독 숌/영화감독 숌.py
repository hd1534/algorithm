# https://www.acmicpc.net/problem/1436

def nextEndNumber(n: int) -> int:
    '''n보다 크고 666이 들어간 수들 중 가장 작은 수'''

    while True:
        n += 1
        sixCounter = 0

        # 6이 3개 연속인거 찾기
        for d in str(n):
            if d == "6":
                if sixCounter == 2:
                    return n
                sixCounter += 1
            else:
                sixCounter = 0


def endNumber(n: int) -> int:
    result = 665

    for _ in range(n):
        result = nextEndNumber(result)

    return result


print(endNumber(int(input())))
