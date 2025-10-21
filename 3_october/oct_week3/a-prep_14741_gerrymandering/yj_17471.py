from itertools import combinations
from collections import deque

# 입력 처리
N = int(input())
population = list(map(int, input().split()))
graph = [[] for _ in range(N + 1)]

# 그래프 인접관계 입력받기
for i in range(1, N + 1):
    data = list(map(int, input().split()))
    for neighbor in data[1:]:
        graph[i].append(neighbor)

# 연결 여부 확인 (BFS)
def is_connected(group):
    visited = set()  # 방문여부
    Q = deque([group[0]])
    visited.add(group[0])
    while Q:
        cur = Q.popleft()
        for neighbor in graph[cur]:
            if neighbor in group and neighbor not in visited:  # 이웃이 그룹 내에 있고, 방문하지 않았다면
                visited.add(neighbor)
                Q.append(neighbor)
    return len(visited) == len(group)  # 방문 그룹 개수 == 실제 인접 그룹 개수이면 True 반환

# 인구 수 계산
def population_sum(group):
    return sum(population[i - 1] for i in group)  # group 인덱스는 1부터, population 인덱스는 0부터

# 메인 로직
areas = [i + 1 for i in range(N)]  # [1, 2, 3, 4, 5, 6]
min_diff = float('inf')

for r in range(1, N // 2 + 1):
    for comb in combinations(areas, r):
        group_a = list(comb)
        group_b = list(set(areas) - set(group_a))

        if is_connected(group_a) and is_connected(group_b):  # 둘 다 연결되어 있으면
            diff = abs(population_sum(group_a) - population_sum(group_b))  # 둘의 인구수 차이를 계산한다
            min_diff = min(min_diff, diff)  # 최소 인구수를 갱신

# 결과 출력
print(min_diff if min_diff != float('inf') else -1)  # 갱신된 적 없으면 -1 출력 (연결되지 않았음)