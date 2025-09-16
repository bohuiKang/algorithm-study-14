import sys; sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):

    def cleaning(r, c, way):
        global clean

        # 주변에 빈칸이 있을 때 => 반시계 90도 한칸 전진
        for mt in range(3, -1, -1): # 3 2 1 0
            look = (mt + way) % 4
            nr = r + dr[look]
            nc = c + dc[look]
            if room[nr][nc] == 0:
                room[nr][nc] = 2
                clean += 1
                cleaning(nr, nc, look)
                break

        # 주변에 빈칸이 없을 때 => 현재 방향 뒤로 후진(벽 있으면 중단)
        else:
            back = (way + 2) % 4
            nr = r + dr[back]
            nc = c + dc[back]
            if room[nr][nc] == 1: # 벽이면 return(중단)
                return
            else: # 벽이 아니면
                cleaning(nr, nc, way)


    N, M = map(int, input().split())
    i, j, d = map(int, input().split())
    room = [list(map(int, input().split())) for _ in range(N)]
    dr = [-1, 0, 1, 0] # 0.북 1.동 2.남 3.서
    dc = [0, 1, 0, -1]

    clean = 1 # 청소 칸 개수 저장 변수
    room[i][j] = 2 # 로봇의 현재 위치 청소 완료
    cleaning(i, j, d) # 로봇의 위치, 바라보는 방향

    print(clean)

