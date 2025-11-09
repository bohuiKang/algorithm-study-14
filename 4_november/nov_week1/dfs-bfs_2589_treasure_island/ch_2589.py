# bfs로 탐색때마다 시간 +1 하고 완탐하면서 최댓값 갱신
from collections import deque
N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

graph = {}
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ni, nj = dr + i, dc + j
                if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 'L':
                    graph.setdefault((i, j), []).append((ni, nj))
def bfs(start):
    q = deque([start])
    visited = [[float('-inf')] * M for _ in range(N)]
    visited[start[0]][start[1]] = 0
    while q:
        i, j = q.popleft()
        if (i, j) in graph:
            for ni, nj in graph[(i, j)]:
                if visited[ni][nj] == float('-inf'):
                    visited[ni][nj] = visited[i][j] + 1
                    q.append((ni, nj))
    result = 0
    for i in range(N):
        for j in range(M):
            result = max(result, visited[i][j])
    return result

max_v = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            result = bfs((i, j))
            max_v = max(max_v, result)
print(max_v)