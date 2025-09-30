#이거 시간초과 안나는게 용한데

from collections import deque
r, c, t = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(r)]

delta = [(0,1), (0,-1), (1,0), (-1,0)]

visited = [[False]*c for _ in range(r)]

def dust():
    # 계산해야할 값들
    q = deque()

    for dr in range(r):
        for dc in range(c):
            if lst[dr][dc] > 0:
                # 확산된 먼지 양
                d = 0
                for i in range(4):
                    nr = dr+delta[i][0]
                    nc = dc+delta[i][1]
                    if 0 <= nr < r and 0 <= nc < r:
                        if lst[nr][nc] == -1:
                            continue
                        q.append((nr, nc, lst[dr][dc]//5))
                        d += lst[dr][dc]//5
                q.append(dr, dc, -d)

    while q:
        x, y, du = q.popleft()
        lst[x][y] += du

def find_cleaner():
    for dr in range(r):
        for dc in range(c):
            if lst[dr][dc] == -1:
                return (dr,dc)

cleaner_up = find_cleaner()
cleaner_down = (cleaner_up[0]+1,0)

def clean():
    # 계산해야할 값들
    q = deque()

    for dr in range(r):
        for dc in range(c):
            if lst[dr][dc] > 0:
                if dr == cleaner_up[0]:
                    if dc+1 != c:
                        q.append((dr, dc+1, lst[dr][dc]))
                    else:
                        q.append(dr+1, dc, lst[dr][dc])
                if dc == c-1:
                    if dr >= cleaner_up:
                        if dr+1 > 0:
                            q.append((dr-1, dc, lst[dr][dc]))
                        else:
                            q.append((dr, dc-1, lst[dr][dc]))
                    else:
                        if dr+1 < r:
                            q.append((dr+1, dc, lst[dr][dc]))
                        else:
                            q.append((dr, dc-1, lst[dr][dc]))



for _ in range(t):
    dust()
    clean()

# 전체의 합 + 공기청정기(-2)
print(sum(lst)+2)
