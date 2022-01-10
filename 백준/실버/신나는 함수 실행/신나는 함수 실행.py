# https://www.acmicpc.net/problem/9184


def w(memo, a, b, c):

    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if a > 20 or b > 20 or c > 20:
        return w(memo, 20, 20, 20)

    if memo[a][b][c] is None:
        if a < b < c:
            memo[a][b][c] = w(memo, a, b, c-1)\
                + w(memo, a, b-1, c-1) - w(memo, a, b-1, c)
        else:
            memo[a][b][c] = w(memo, a-1, b, c) + w(memo, a-1, b-1, c)\
                + w(memo, a-1, b, c-1) - w(memo, a-1, b-1, c-1)

    return memo[a][b][c]


def sol():
    memo = [[[None for c in range(21)] for b in range(21)] for a in range(21)]

    while True:
        a, b, c = map(int, input().split())
        if a == -1 and b == -1 and c == -1:
            break

        print("w(%d, %d, %d) = %d" % (a, b, c, w(memo, a, b, c)))


if __name__ == "__main__":
    sol()
