from collections import deque

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def bfs(c, r):
    visited = [[-1] * M for _ in range(N)]

    q = deque()
    q.append([c, r])
    visited[c][r] = 0
    temp_max = -float('inf')

    while q:
        cc, cr = q.popleft()
        for i in range(4):
            nc = cc + dc[i]
            nr = cr + dr[i]
            if 0 <= nc < N and 0 <= nr < M and visited[nc][nr] == -1 and arr[nc][nr] == "L":
                visited[nc][nr] = visited[cc][cr] + 1
                temp_max = max(temp_max, visited[nc][nr])
                q.append([nc, nr])

    return temp_max

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
max_distance = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == "L":
            max_distance = max(max_distance, bfs(i, j))

print(max_distance)