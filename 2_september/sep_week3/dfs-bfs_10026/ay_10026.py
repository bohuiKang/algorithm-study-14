# import sys
# sys.stdin = open("input.txt", "r")
#
from collections import deque

dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]] #우하좌상
# T = int(input())
# for tc in range(1, 1+T):
N = int(input())
picture = [input() for _ in range(N)]

def bfs(r, c, color):
    q = deque([(r, c)])

    while q:
        r, c = q.popleft()

        for dr, dc in dirs:
            nr = r + dr
            nc = c + dc
            if nr < 0 or nr >= N or nc < 0 or nc >= N or visited[nr][nc]:
                continue

            if picture[nr][nc] in color:
                visited[nr][nc] = 1 # 같은 색인 경우만 visited에 표시 새로운 구역 확인할때 다시 확인해줘야 하기 때문
                q.append((nr, nc))

# 적록색맹 아닌 사람
visited = [[0] * N for _ in range(N)]
not_gr_blind = 0
for i in range(N): # 새로운 구역 시작 번호 찾기 위한 for 문
    for j in range(N):
        if visited[i][j]:
            continue
        color = [picture[i][j]]
        bfs(i, j, color)
        not_gr_blind += 1

# 적록색맹인 사람
visited = [[0] * N for _ in range(N)]
gr_blind = 0
for i in range(N):
    for j in range(N):
        if visited[i][j]:
            continue
        if picture[i][j] == "R" or picture[i][j] == "G": # 적록 색맹이면 R, G는 같은 구역 취급
            color = ["R", "G"]
        else:
            color = ["B"]
        bfs(i, j, color)
        gr_blind += 1

print(not_gr_blind, gr_blind)









