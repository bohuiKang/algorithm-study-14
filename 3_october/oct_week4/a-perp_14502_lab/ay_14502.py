# import sys
# sys.stdin = open("14502_input.txt", "r")
from collections import deque

drs =[(1, 0), (-1, 0), (0, -1), (0, 1)]

def bfs(r, c):
    q = deque([(r,c)])
    arr[r][c] = 3
    while q:
        r, c = q.popleft()
        for dr, dc in drs:
            nr, nc = r + dr, c + dc
            if nr < 0 or nr >= N or nc < 0 or nc >= M or arr[nr][nc]:
                continue
            q.append((nr, nc))
            arr[r][c] = 3



N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]


# 벽 위치 고르기
max_val = 0
def sellect_walls(sr, sc, cnt, walls):
    global max_val
    if cnt == 3:
        check_arr = [row[:] for row in arr]
        for nr, nc in walls:
            check_arr[nr][nc] = 1

        for r in range(N):
            for c in range(M):
                if check_arr[r][c] == 2:
                    bfs(r, c)

        cnt = 0
        for r in range(N):
            for c in range(M):
                if arr[r][c] == 0:  # 0이면
                    cnt += 1
        max_val = max(cnt, max_val)
        return

    for r in range(sr, N):
        for c in range(sc if r == sr else 0, M):
            if not arr[r][c]:
                sellect_walls(r, c, cnt+1, walls+[(r,c)])

sellect_walls(0, 0, 0, [])
print(max_val)
