import sys
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
r, c, d = map(int, input().split())
dr = [-1, 0, 1, 0] # 북, 동, 남, 서
dc = [0, 1, 0, -1]

floors = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
while True:

    if floors[r][c] == 0: # 청소안된 바닥이면 청소하기
        floors[r][c] = 2
        cnt += 1

    for i in range(1, 5): # 4방향 확인
        nd = (d-i) % 4
        nr = r + dr[nd]
        nc = c + dc[nd]

        if floors[nr][nc] != 0: # 벽이거나 청소한곳이면 건너뛰기
            continue

        if floors[nr][nc] == 0: # 청소해야 하는 바닥이면 위치, 방향 바꾸고
            r = nr
            c = nc
            d = nd
            break
    else:
        idx = d-2
        r = r + dr[idx]
        c = c + dc[idx]

        if floors[r][c] == 1: # 벽이면 종료
            break

print(cnt)

