R, C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]

for r in range(R): # 공기 청정기 위치 찾기
    if room[r][0] == -1:
    air_cleaner = [(r,0), (r+1,0)]
    break
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 먼지 확산
def dust(now_room):
    new_room = [[0]*C for _ in range(R)]
    for r in range(R):
        for c in range(C):

            if now_room[r][c] == 1 or now_room[r][c] == -1:
                continue
            dust_all = now_room[r][c]
            dust_mini = dust_all // 5

            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if nr < 0 or nr >= R or nc < 0 or nc >= C:
                    continue
                new_room[nr][nc] += dust_mini
                dust_all -= dust_mini
            new_room[r][c] += dust_all
    return new_room

def flow(now_room): # 공청기 돌리기
    new_room = [[0]*C for _ in range(R)]





for i in range(T):
    dust(room)
    flow(room)





