'''
#0: 북쪽 1:동쪽 2:남쪽 3:서쪽
delta = [[-1,0], [1,0], [0,1], [-1,0]]

n, m = map(int, input().split())
r, c, d = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]

def clean(now_r, now_c, direction, cnt):

    #현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
    if lst[now_r][now_c] == 0:
        cnt += 1
        #청소표시
        lst[now_r][now_c] = 2

    for i in range(4):
        # 4칸중 청소되지 않은 빈 칸이 있는경우
        if lst[now_r+delta[i][0]][now_c+delta[i][1]] == 0:
            #반시계방향으로 90도 회전
            di = (direction+3)%4
            #바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
            next_r = now_r+delta[di][0]
            next_c = now_c+delta[di][1]
            if 0 <= next_r < n and 0 <= next_c < m:
                if lst[next_r][next_c] == 0:
                    clean(next_r, next_c, di, cnt)
            break
    else: #4칸중 빈칸이 없는 경우
        next_r = now_r+delta[(direction+1)%4][0]
        next_c = now_c+delta[(direction+1)%4][1]
        if 0 <= next_r < n and 0 <= next_c < m:
            if lst[next_r][next_c] != 1:
                clean(next_r, next_c, direction, cnt)
            else:
                return cnt

print(clean(r, c, d, 0))
'''
#0:북쪽 1:동쪽 2:남쪽 3:서쪽
delta = [(-1,0), (0,1), (1,0), (0,-1)]

n, m = map(int, input().split())
r, c, d = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]
cnt = 0

def clean(now_r, now_c, direction):
    global cnt

    #현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
    if lst[now_r][now_c] == 0:
        cnt += 1
        #청소표시
        lst[now_r][now_c] = 2

    # 4칸중 청소되지 않은 빈 칸이 있는경우
    for i in range(1, 5):
        #반시계 방향으로 회전
        di = (direction+(3*i))%4
        next_r = now_r + delta[di][0]
        next_c = now_c + delta[di][1]
        if 0 <= next_r < n and 0 <= next_c < m:
            # 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
            if lst[next_r][next_c] == 0:
                clean(next_r, next_c, di)
                break

    #만약 for문이 break없이 모두 실행된다면
    else: #4칸중 빈칸이 없는 경우이다.
        #바라보는 방향을 유지한 채로 한 칸 후진
        di = (direction+2)%4
        next_r = now_r+delta[di][0]
        next_c = now_c+delta[di][1]
        if 0 <= next_r < n and 0 <= next_c < m:
            #후진할 수 있다면 후진
            if lst[next_r][next_c] != 1:
                clean(next_r, next_c, direction)
            #없다면 종료
            else:
                return

clean(r, c, d)
print(cnt)