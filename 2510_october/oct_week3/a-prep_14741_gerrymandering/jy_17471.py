from itertools import combinations
from collections import deque


def bfs(comb):
    q = deque()
    # 조합의 가장 첫번째를 시작점으로 지정
    q.append(comb[0])
    # 탐색 효율 증가를 위해 list를 set로 변환
    visited = {comb[0]}

    while q:
        curr = q.popleft()
        for nxt in neighbor[curr]:
            if nxt in comb and nxt not in visited:
                visited.add(nxt)
                q.append(nxt)

    # visited에 남아있는 원소들이 comb(=set_a(b))와 같다면 서로 연결되어 있음
    # visited == set(comb) 이면 True 아니면 False를 반환함
    return visited == set(comb)


N = int(input())
arr = [i for i in range(N)]
# 각 지역의 인구 수
population = list(map(int, input().split()))
# 이웃하는 정보 기록
neighbor = [[] for _ in range(N)]
answer = float('inf')

for i in range(N):
    temp = list(map(int, input().split()))
    for x in temp[1:]:
        # 각 구역과 인접한 구가 기록되어있음
        neighbor[i].append(x - 1)

# combination에 넣으려고 만들었음
arr = [k for k in range(N)]

# 절반만 탐색하면 되기에 범위를 N // 2 + 1로 지정
for i in range(1, N // 2 + 1):
    for comb in combinations(arr, i):
        set_a = set(comb)
        set_b = set(range(N)) - set_a

        if bfs(list(set_a)) and bfs(list(set_b)):
            sum_a = sum(population[j] for j in set_a)
            sum_b = sum(population[j] for j in set_b)
            answer = min(answer, abs(sum_a - sum_b))

if answer == float('inf'):
    print(-1)
else:
    print(answer)