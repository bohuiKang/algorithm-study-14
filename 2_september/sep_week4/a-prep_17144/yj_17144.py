from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

R, C, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)] # 미세먼지의 초기 양

# 공기청정기 위치 찾기
air_purifier = []

for _ in range(T):  # T초 돌리기

    # 1. 미세먼지 확산
    # 먼지값 넣기 - BFS 돌기를 T번 하기
    # -------------------------------- 먼지 확산 시작 --------------------------------
    # 큐에 초기 먼지값 넣기
    Q = deque([])
    next_board = [[0] * C for _ in range(R)]  # 1초 퍼진 후의 먼지값
    for i in range(R):
        for j in range(C):
            if board[i][j] > 0:
                curX, curY = i, j
                mini_dust = board[curX][curY] // 5  # 확산되는 먼지 양
                cnt = 0  # 확산되는 먼지 칸 수
                for dir in range(4):
                    nx = curX + dx[dir]
                    ny = curY + dy[dir]
                    if nx < 0 or nx >= R or ny < 0 or ny >= C: continue  # 범위 밖은 pass
                    if board[nx][ny] == -1: continue  # 공청기 있는곳은 pass
                    cnt += 1  # 먼지 퍼지기 가능한 곳이면 퍼지기
                    next_board[nx][ny] += mini_dust
                next_board[curX][curY] += (board[curX][curY] - mini_dust * cnt)
            elif board[i][j] == -1:  # 공기청정기 위치 찾기
                air_purifier.append([i, j])


    # -------------------------------- 여기까지 먼지 확산 --------------------------------
    # -------------------------------- 공청기 순환 시작 --------------------------------
    # 위쪽
    air1 = air_purifier[0][0]
    # 1. 아래
    # 위쪽 공청기 윗칸 윗칸부터 옮기기(두 칸 위)
    for i in range(air1 - 2, -1, -1):
        next_board[i + 1][0] = next_board[i][0]
    # 2. 왼쪽
    for i in range(1, C):
        next_board[0][i - 1] = next_board[0][i]
    # 3. 위
    for i in range(1, air1 + 1):
        next_board[i - 1][C - 1] = next_board[i][C - 1]
    # 4. 오른쪽
    for i in range(C - 2, 0, -1):
        next_board[air1][i + 1] = next_board[air1][i]
    next_board[air1][1] = 0

    # 아래쪽
    air2 = air_purifier[1][0]
    # 1. 위
    for i in range(R - air2 + 1, R):
        next_board[i - 1][0] = next_board[i][0]
    # 2. 왼쪽
    for i in range(1, C):
        next_board[R - 1][i - 1] = next_board[R - 1][i]
    # 3. 아래
    for i in range(R - 1, air2, -1):
        next_board[i][C - 1] = next_board[i - 1][C - 1]
    # 4. 오른쪽
    for i in range(C - 2, 0, -1):
        next_board[air2][i + 1] = next_board[air2][i]
    next_board[air2][1] = 0
    # for x in next_board:
    #     print(*x)
    # next_board를 board로 옮기기
    for i in range(R):
        for j in range(C):
            if board[i][j] == -1: continue
            else:
                board[i][j] = next_board[i][j]
# -------------------------------- 공청기 순환 끝 --------------------------------
# 남아있는 먼지 양 출력
result = 2  # 공청기 값 미리 빼주기
for i in range(R):
    for j in range(C):
        result += board[i][j]

print(result)