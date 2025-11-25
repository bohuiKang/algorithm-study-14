from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def cnt_cheese():
    """치즈가 몇 개 있는지 센다."""
    cnt_c = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                cnt_c += 1
    return cnt_c

def bfs():
    global cur_cheese_cnt

    # 바깥 공기 부분을 bfs 돌려서 구하기
    # 초기화
    Q = deque([(0, 0)])
    visit[0][0] = 1
    melt = deque([])  # 녹일 치즈들

    while Q:
        curX, curY = Q.popleft()
        for dir in range(4):
            nx = curX + dx[dir]
            ny = curY + dy[dir]
            if nx < 0 or nx >= N or ny < 0 or ny >= M: continue  # board 범위 밖이면 pass
            if visit[nx][ny] == 1: continue  # 방문한 곳이면 pass
            visit[nx][ny] = 1  # 방문하기
            if board[nx][ny] == 1:  # 만약 치즈(1)면 melt에 append하기
                melt.append((nx, ny))
            elif board[nx][ny] == 0:  # 바깥 공기(0)면 Q에 넣기
                Q.append((nx, ny))
    
    # melt에 있는 것들 녹이기
    for x, y in melt:
        board[x][y] = 0

    return len(melt)

N, M = map(int, input().split())  # 세로, 가로 길이
board = [list(map(int, input().split())) for _ in range(N)]  # 판 입력받기, 바깥 공기 = 2
cur_cheese_cnt = 0  # 현재 남아있는 치즈 수

cur_cheese_cnt = cnt_cheese()  # 원래 치즈 개수 세기

# bfs 돌리기
time = 1
while True:
    visit = [[0] * M for _ in range(N)]
    melt_cnt = bfs()  # 녹은 치즈 개수
    cur_cheese_cnt -= melt_cnt
    if cur_cheese_cnt == 0:  # 치즈를 다 녹였으면
        print(time)
        print(melt_cnt)  # 녹기 한 시간 전에 남아있는 치즈조각 칸 개수
        break
    time += 1
