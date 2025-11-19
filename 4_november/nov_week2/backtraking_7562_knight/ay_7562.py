import sys
from collections import deque
sys.stdin = open("7562_input.txt", "r")

T = int(input())

# 상하좌우 방향이동
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우

def move2(dr, dc): # 상하좌우에서 2차 이동
    if dr == 0:
        dc += dc
        return [(1, dc), (-1, dc)]
    else:
        dr += dr
        return [(dr, 1), (dr, -1)]

def bfs(r, c):
    q = deque([(r, c, 0)])
    visited[r][c] = 1

    while q:
        r, c, cnt = q.popleft()
        if r == fr and c == fc:
            return cnt

        for dr, dc in dirs:
            for ndr, ndc in move2(dr, dc):
                nr, nc = r + ndr, c + ndc
                if nr < 0 or nr >= I or nc < 0 or nc >= I or visited[nr][nc]:
                    continue
                q.append((nr, nc, cnt+1))
                visited[nr][nc] = 1


for tc in range(1, 1+T):
    I = int(input())
    sr, sc = map(int, input().split())
    fr, fc = map(int, input().split())
    visited = [[0]*I for _ in range(I)]


    print(bfs(sr, sc))
