from collections import deque
import sys

input = sys.stdin.readline

dc = [0, 1, 0, -1]
dr = [1, 0, -1, 0]

def bfs(c, r, arr, visited):
    q = deque([(c, r)])

    while q:
        cc, cr = q.popleft()

        for i in range(4):
            mc = cc + dc[i]
            mr = cr + dr[i]

            if 0 <= mr < N and 0 <= mc < N and not visited[mc][mr]:
                if arr[mc][mr] == arr[cc][cr]:
                    visited[mc][mr] = True
                    q.append((mc, mr))

    return 1

N = int(input())
b_arr = [list(input()) for _ in range(N)]
rg_arr = [[c if c != "R" else "G" for c in row] for row in b_arr]
b_visited = [[False] * N for _ in range(N)]
rg_visited = [[False] * N for _ in range(N)]
b_cnt = rg_cnt = 0

for i in range(N):
    for j in range(N):
        if not b_visited[i][j]:
            b_visited[i][j] = True
            b_cnt += bfs(i, j, b_arr, b_visited)

for i in range(N):
    for j in range(N):
        if not rg_visited[i][j]:
            rg_visited[i][j] = True
            rg_cnt += bfs(i, j, rg_arr, rg_visited)

print(b_cnt, rg_cnt)