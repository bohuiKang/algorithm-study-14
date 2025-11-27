# 안전영역 탐색용 stack dfs, 그리고 바이러스가 퍼져나갈 재귀 recur를 각각 만듬
# arr에 2차원 배열로 input
# graph에 setdefault를 사용해 간선할당
# 바이러스 퍼져나가는 recur를 2중 for문으로 arr중 시작위치의 값이 2인곳에서 상하좌우 델타의 arr값이 0일때 퍼져나가게 함
# 마지막에 2중 for문으로 dfs를 돌려 안전영역의 크기를 구하여 출력

from itertools import combinations

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 상하좌우 델타
delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# 그래프 간선할당
graph = {}
for i in range(N):
    for j in range(M):
        if arr[i][j] != 1:  # 벽이 아니면
            for dr, dc in delta:
                ni, nj = i + dr, j + dc
                if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != 1:
                    graph.setdefault((i, j), []).append((ni, nj))

# 바이러스 확산용 (재귀)
def spread(i, j, grid_copy):
    for dr, dc in delta:
        ni, nj = i + dr, j + dc
        if 0 <= ni < N and 0 <= nj < M and grid_copy[ni][nj] == 0:
            grid_copy[ni][nj] = 2
            spread(ni, nj, grid_copy)

# 안전영역 탐색용 (dfs)
def dfs(start, grid_copy):
    stack = [start]
    cnt = 0
    while stack:
        i, j = stack.pop()
        if grid_copy[i][j] != 0:
            continue
        grid_copy[i][j] = -1  # 방문 표시
        cnt += 1
        if (i, j) in graph:
            for ni, nj in graph[(i, j)]:
                if grid_copy[ni][nj] == 0:
                    stack.append((ni, nj))
    return cnt

# 벽 세우기 조합 및 계산
empty_arr = [(i, j) for i in range(N) for j in range(M) if arr[i][j] == 0]
virus = [(i, j) for i in range(N) for j in range(M) if arr[i][j] == 2]

max_safe = 0
for walls in combinations(empty_arr, 3):
    grid_copy = [row[:] for row in arr]  # grid_copy 사용
    for wi, wj in walls:
        grid_copy[wi][wj] = 1  # 벽 세움

    # 바이러스 확산
    for vi, vj in virus:
        spread(vi, vj, grid_copy)

    # 안전영역 크기 계산
    safe = 0
    for i in range(N):
        for j in range(M):
            if grid_copy[i][j] == 0:
                safe += dfs((i, j), grid_copy)

    max_safe = max(max_safe, safe)

print(max_safe)