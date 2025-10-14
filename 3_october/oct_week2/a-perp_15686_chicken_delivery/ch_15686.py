# 각집에서 bfs를 돌리면 가장 가까운 치킨집까지의 치킨거리를 구할 수 있음
# M개의 치킨집만 선택하는 모든 경우의 수에서 치킨거리 최솟값 구하기?
from collections import deque
from itertools import combinations
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

def bfs(start):
    q = deque([start])
    visited = [[0] * N for _ in range(N)]
    while q:
        r, c = q.popleft()
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] < 2:
                    visited[nr][nc] = visited[r][c] + 1
                    q.append((nr, nc))
                if arr[nr][nc] == 2:
                    return visited[r][c] + 1

# 치킨집(2)들의 좌표를 리스트에 담음
list_of_2 = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            list_of_2.append((i, j))

# 선택된 치킨집들의 좌표 경우의 수
comb = list(combinations(list_of_2, M))

min_v = float('inf')

for chicken_list in comb:
    # 선택된 치킨집만 2로, 나머지 치킨집은 0으로 초기화
    temp = [row[:] for row in arr]
    for r, c in list_of_2:
        temp[r][c] = 0
    for r, c in chicken_list:
        temp[r][c] = 2

    # 각 집에서 BFS 돌려 치킨 거리 합 구하기
    city_distance = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                arr = temp
                city_distance += bfs((i, j))

    min_v = min(min_v, city_distance)

print(min_v)