'''
comb = []
path = [0]*m
# 치킨집을 m개 조합으로 고른 후 치킨 거리 계산 완탐
def recur(idx, cnt, path):

    # m개 다 골랐으면
    if cnt == m:
        comb.append(tuple(path))
        return

    # 인덱스 초과시 중단
    if idx >= c_num:
        return

    # 안 고른 경우
    recur(idx+1, cnt, path)

    # 해당 치킨집을 고른 경우
    path[cnt] = idx
    recur(idx+1, cnt+1, path)


def cal(cnt, d):
    global min_d
    for  in combs
    # 가지치기, 최소거리보다 길다면 중단
    if min_d <= d:
        continue

    # m개를 다 골랐으면 최소거리 갱신
    if cnt == m:
        min_d = d
        continue


'''

from itertools import combinations

n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]

# 집 위치 목록
houses = []
# 치킨집 위치 목록
chicken = []

for r in range(n):
    for c in range(n):
        if lst[r][c] == 1:
            houses.append((r, c))
        elif lst[r][c] == 2:
            chicken.append((r, c))
# 최소 거리
min_d = float('inf')
c_num = len(chicken)

# 치킨집 m개를 선택하는 조합
for chickens in combinations(chicken, m):
    total = 0
    # 각 집에 대해 가장 가까운 치킨집 거리 계산
    for hx, hy in houses:
        # 각 집당 최소 치킨 거리 계산
        dist = min(abs(hx - cx) + abs(hy - cy) for cx, cy in chickens)
        total += dist
        # 만약 현재 최소거리보다 total값이 크다면 중단
        if total > min_d:
            break
    # 중단되지않고 끝까지 돌았다면 현재 최소 거리보다 작은 total값, 최소 거리 갱신
    else:
        min_d = total

print(min_d)