#n = 국가의 수, m = 순위를 알아볼 국가의 인덱스
n, m = map(int, input().split())
medal_lst = [list(map(int, input().split())) for _ in range(n)]
ranking = []
medal = 1

def find_medal(medal_lst, medal):
    rank = 1
    max_medal = 0

    if len(ranking) == n:
        return

    for i in range(n):
        if medal_lst[i][medal] < max_medal:
            max_medal = medal_lst[i][medal]
            max_medal_idx = i

    same = []

    for j in range(n):
        if medal_lst[j][1] == max_medal:
            same.append(medal_lst[j])

    if len(same) == 1:
        ranking.append([rank] + medal_lst(max_medal_idx))
        rank += 1
        medal_lst.pop(i)
        medal = 1
        find_medal(medal_lst, medal)

    else:
        if medal == 3:
            for k in range(len(same)):
                ranking.append([rank] + same[k])
                medal_lst.pop(same[0])
                medal = 1
                find_medal(medal_lst, medal)

        medal += 1
        find_medal(same, medal)

find_medal(medal_lst, medal)