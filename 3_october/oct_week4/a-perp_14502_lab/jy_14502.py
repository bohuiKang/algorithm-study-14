from itertools import combinations
from collections import deque

dc = [0, 1, 0, -1]
dr = [1, 0, -1, 0]

def infection(temp):
    q = deque(virus)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dc[i], y + dr[i]
            if 0 <= nx < N and 0 <= ny < M and temp[nx][ny] == 0:
                temp[nx][ny] = 2
                q.append((nx, ny))

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

empty = [(i, j) for i in range(N) for j in range(M) if arr[i][j] == 0]
virus = [(i, j) for i in range(N) for j in range(M) if arr[i][j] == 2]

answer = 0

for walls in combinations(empty, 3):
    temp = [row[:] for row in arr]
    for x, y in walls:
        temp[x][y] = 1
    infection(temp)
    safe = sum(row.count(0) for row in temp)
    answer = max(answer, safe)

print(answer)