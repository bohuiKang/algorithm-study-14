N , K = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

n, k = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]
#lst[idx][0] = 국가 번호 lst[idx][1] = 금메달
#등수 = 자신보다 더 잘한 나라의 수 +1
#금메달 수로 1~N 등수 배정
#등수가 같으면 은메달 비교, 은메달 같으면 동메달 비교, 같으면 같은 등수
max_gold = 0
for i in range(n):
    if max_gold < lst[i][0]:

