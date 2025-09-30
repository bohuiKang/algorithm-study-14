import sys; sys.stdin = open('input.txt', 'r')

dr, dc = [0, 1, 0, -1], [1, 0, -1, 0] # 우하좌상

def dirty_more(sr, sc):
    num = dirty[sr][sc] // 5
    cnt = 0
    for d in range(4):
        nr = sr + dr[d]
        nc = sc + dc[d]
        if 0 <= nr < R and 0 <= nc < C:
            if dirty[nr][nc] != -1:
                cnt += 1
                spread[nr][nc] += num
    spread[sr][sc] += (dirty[sr][sc] - (num * cnt))


def air_purifier(time, up_r, down_r):
    get_dust = 0

    # up
    rr = up_r
    cc = 0
    tt, dust = up(0, rr, cc, time)
    get_dust += dust

    if tt > 0:
        tt, dust = right(rr, cc, tt)
        get_dust += dust

    if tt > 0:
        tt, dust = down(rr, cc, tt)
        get_dust += dust

    if tt > 0:
        tt, dust = left(rr, cc, tt)
        get_dust += dust

    # down
    rr = down_r
    cc = 0
    down(rr, cc, tt)
    if tt > 0:
        tt, dust = right(rr, cc, tt)
        get_dust += dust

    if tt > 0:
        tt, dust = up(rr, cc, tt)
        get_dust += dust

    if tt > 0:
        tt, dust = left(rr, cc, time)
        get_dust += dust

    return get_dust

def up(limit, rr, cc, tt):
    clean = 0
    while rr >= limit: # 위
        rr -= 1
        if spread[rr][cc] > 0:
            clean += spread[rr][cc]
    return tt, clean

def right(rr, cc, tt):
    clean = 0
    while cc < C: # 오른
        cc += 1
        if spread[rr][cc] > 0:
            clean += spread[rr][cc]
    return tt, clean

def down(limit, rr, cc, tt):
    clean = 0
    while rr <= limit: # 아래
        rr += 1
        if spread[rr][cc] > 0:
            clean += spread[rr][cc]
    return tt, clean

def left(rr, cc, tt):
    clean = 0
    while cc >= 1: # 왼
        rr -= 1
        if spread[rr][cc] > 0:
            clean += spread[rr][cc]
    return tt, clean



T = int(input())
for tc in range(1, T+1):
    R, C, K = map(int, input().split()) # 가로R 세로C 작동K초
    dirty = [list(map(int, input().split())) for _ in range(R)]
    spread = [[0]*C for _ in range(R)]
    dusts = 0
    machine = []
    # 먼지 확산
    for x in range(R):
        for y in range(C):
            if dirty[x][y] > 0:
                dusts += dirty[x][y]
                dirty_more(x, y)
            elif dirty[x][y] == -1: # 공기 청정기 위치 복사
                machine.append(x)
                spread[x][y] = -1

    # 공청 동작
    print(dusts - air_purifier(K, *machine))
