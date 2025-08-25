#n = 국가의 수, m = 순위를 알아볼 국가의 인덱스
<<<<<<< HEAD
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
=======
def find_ranking(arr, i, rank_num):
    m = 0
    same = []

    if len(medal_lst) == 0:
        return rank

    for k in range(len(arr)):
        if medal_lst[k][i] > m:
            m = medal_lst[k][i] #지금 해당 메달(금/은/동)에서 가장 높은 메달 수

    for kk in range(len(arr)):
        if medal_lst[kk][i] == m:
            same_max = arr[kk]
            same_max_idx = kk
            same.append(same_max) #같은거 저장

    if len(same) == 1:
        rank.append([same_max[0], rank_num]) #이렇게 되면 rank 내에서 i의 인덱스 번호 +1 = 순위가 되어 따로 지정할 필요 없음.. 아마?
        medal_lst.pop(same_max_idx)
        i = 1
        rank_num += 1
        find_ranking(medal_lst, i, rank_num)

    else:
        if i == 3:
            for j in range(len(same)):
                rank.append([same_max[j][0], rank_num])
            medal_lst.pop(same_max[0])
            rank_num += 1
            i = 1
            find_ranking(same, i, rank_num)
        else: #
            find_ranking(same, i+1, rank_num)

n, m = map(int, input().split())
medal_lst = [list(map(int, input().split())) for _ in range(n)]
rank = []

rank_num = 1
i = 1

print(find_ranking(medal_lst, i, rank_num))

여러분 죄송합니다 못 풀겠어요 ~!!!!
졸업식 하고 나서 제대로 풀어보겠습니다 ~!!!!
잘 지내세요 ~!!!!

















>>>>>>> 9bf5c4bdb2024d863805fcbe3b5f4f70cf8330e5

find_medal(medal_lst, medal)