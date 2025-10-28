def dfs(start):
    stack = [start]
    while stack:
        i, j = stack.pop()
        if grid_copy[i][j] == -1:  # visited 역할
            continue
        grid_copy[i][j] = -1
        if (i, j) in graph:
            nxt = graph[(i, j)]
            stack.extend(nxt)
    return 1

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
rains = max(max(row) for row in arr) # 지역 최대 높이 = 비가 오는 최대 높이

max_v = 0
for rain in range(rains):
    grid_copy = [row[:] for row in arr] # 이번 케이스에 사용할 지역 복사
    for i in range(N):
        for j in range(N):
            if grid_copy[i][j] <= rain: # 비에 잠긴 지역 -1로 표시
                grid_copy[i][j] = -1
    # 간선할당
    graph = {}
    delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for i in range(N):
        for j in range(N):
            if grid_copy[i][j] != -1:
                for dr, dc in delta:
                    ni, nj = i + dr, j + dc
                    if 0 <= ni < N and 0 <= nj < N and grid_copy[ni][nj] != -1:
                        graph.setdefault((i, j), []).append((ni, nj))

    # dfs 탐색
    result = 0
    for i in range(N):
        for j in range(N):
            if grid_copy[i][j] == -1:
                continue
            result += dfs((i, j))
    max_v = max(max_v, result)

print(max_v)