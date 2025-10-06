dx = [-1, 0, 1, 0]  # 북, 동, 남, 서
dy = [0, 1, 0, -1]

N, M = map(int, input().split())   # N와 M 입력받기 (방 크기)
r, c, d = map(int, input().split())  # 로봇 청소기 좌표 (r, c)와 처음 로청의 방향 d
# 방의 상태 입력받기 (N*M)  0 = 청소 안 된 빈 칸, 1 = 벽, 2 = 청소된 빈 칸
board = [list(map(int, input().split())) for _ in range(N)]

# 로봇청소기 작동
curX, curY = r, c  # 현재 좌표 초기화
clean = 0  # 청소한 영역의 개수 초기화
while True:
    # 1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
    if board[curX][curY] == 0:
        board[curX][curY] = 2  # 2는 청소했다는 표시
        clean += 1

    # 3번 반시계 방향으로 회전하며 청소하지 않은 칸 탐색 - 청소 안된 곳 없으면 제자리로 돌아올테니까!
    for _ in range(4):
        d = (d + 3) % 4  # 1. 반시계 방향으로 90도 회전한다. == 시계 방향으로 270도 회전한다.
        nx = curX + dx[d]
        ny = curY + dy[d]
        if nx < 0 or nx >= N or ny < 0 or ny >= M: continue  # 범위 안에 있는지 확인
        if board[nx][ny] == 1 or board[nx][ny] == 2: continue  # 벽이 아닌지, 이미 청소했는지 확인

        # 2. 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
        curX, curY = nx, ny
        break  # 3. 1번으로 돌아간다.

    else:  # 2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
        ndx = curX + dx[d] * (-1)   # 후진
        ndy = curY + dy[d] * (-1)
        if ndx < 0 or ndx >= N or ndy < 0 or ndy >= M: break  # 범위 안에 있는지 확인
        # 2. 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
        if board[ndx][ndy] == 1: break
        else:  # 벽이 없다면:
            curX, curY = ndx, ndy  # 1. 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.

print(clean)  # 청소하는 영역의 개수를 구하라.