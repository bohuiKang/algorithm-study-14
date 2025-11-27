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
                    if 0 <= nr < r and 0 <= nc < c:
                        if lst[nr][nc] == -1:
                            continue
                        q.append((nr, nc, lst[dr][dc]//5))
                        d += lst[dr][dc]//5
                q.append((dr, dc, -d))

    while q:
        x, y, du = q.popleft()
        lst[x][y] += du

def find_cleaner():
    for dr in range(r):
        for dc in range(c):
            if lst[dr][dc] == -1:
                return dr,dc

cleaner_up = find_cleaner()
cleaner_down = (cleaner_up[0]+1,0)
'''
def clean():
    # 계산해야할 값들
    q = deque()

    for dr in range(r):
        for dc in range(c):
            #공기청정기가 아닌 먼지를 만났을때
            if lst[dr][dc] > 0:
                if dr == cleaner_up[0]:
                    if dc+1 != c:
                        q.append((dr, dc+1, lst[dr][dc]))
                    else:
                        q.append((dr-1, dc, lst[dr][dc]))
                elif dc == c-1:
                    if dr >= cleaner_up[0]:
                        if dr+1 > 0:
                            q.append((dr-1, dc, lst[dr][dc]))
                        else:
                            q.append((dr, dc-1, lst[dr][dc]))
                    else:
                        if dr+1 < r:
                            q.append((dr+1, dc, lst[dr][dc]))
                        else:
                            q.append((dr, dc-1, lst[dr][dc]))
                elif dr == cleaner_down[0]:
                    if dc+1 != c:
                        q.append((dr, dc+1, lst[dr][dc]))
                    else:
                        q.append((dr+1, dc, lst[dr][dc]))
                elif dc == 0:
                    if dr > cleaner_up[0]:
                        if dr+1 == cleaner_up:
                            continue
                        else:
                            q.append((dr+1, dc, lst[dr][dc]))
                    else:
                        if dr-1 == cleaner_down[0]:
                            continue
                        else:
                            q.append((dr-1, dc, lst[dr][dc]))
                lst[dr][dc] = 0
    while q:
        x, y, du = q.popleft()
        lst[x][y] += du
'''
def clean():
    up, _ = cleaner_up
    down, _ = cleaner_down

    # 위쪽 반시계
    for i in range(up-1, 0, -1):   # 아래 -> 위
        lst[i][0] = lst[i-1][0]
    for i in range(c-1):           # 왼 -> 오
        lst[0][i] = lst[0][i+1]
    for i in range(up):            # 위 -> 아래
        lst[i][c-1] = lst[i+1][c-1]
    for i in range(c-1, 1, -1):    # 오 -> 왼
        lst[up][i] = lst[up][i-1]
    lst[up][1] = 0  # 공기청정기 옆칸은 먼지 없음

    # 아래쪽 시계
    for i in range(down+1, r-1):   # 위 -> 아래
        lst[i][0] = lst[i+1][0]
    for i in range(c-1):           # 왼 -> 오
        lst[r-1][i] = lst[r-1][i+1]
    for i in range(r-1, down, -1): # 아래 -> 위
        lst[i][c-1] = lst[i-1][c-1]
    for i in range(c-1, 1, -1):    # 오 -> 왼
        lst[down][i] = lst[down][i-1]
    lst[down][1] = 0  # 공기청정기 옆칸은 먼지 없음



for _ in range(t):
    dust()
    clean()

result = sum(sum(row) for row in lst)

# 전체의 합 + 공기청정기(-2)
print(result+2)
