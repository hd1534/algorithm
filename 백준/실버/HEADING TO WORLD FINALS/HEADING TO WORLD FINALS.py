# https://www.acmicpc.net/problem/10981

n, k = map(int, input().split())

dic: dict[str, list] = {}
for i in range(n):
    univ, team, solved, penalty = input().split()
    solved = int(solved)
    penalty = int(penalty)

    if univ not in dic or solved > dic[univ][0] or solved == dic[univ][0] and penalty < dic[univ][1]:
        dic[univ] = [solved, penalty, team]


for solved, penalty, team in sorted(dic.values(), key=lambda t: [-t[0], t[1]])[:k]:
    print(team)
