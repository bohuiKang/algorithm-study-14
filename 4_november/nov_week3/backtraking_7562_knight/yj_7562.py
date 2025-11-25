from collections import deque

dx = [1, 1, 2, 2, -1, -1, -2, -2]
dy = [2, -2, 1, -1, 2, -2, 1, -1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # board[N][N], 체스판 크기
    curX, curY = map(int, input().split())  # 현재 나이트가 있는 칸 좌표
    destX, destY = map(int, input().split())  # 나이트가 이동하려고 하는 목표 지점 좌표
    board = [[-1] * N for _ in range(N)]  # 거리 기록한 체스판

    # 시작점 초기화
    board[curX][curY] = 0
    Q = deque([(curX, curY)])

    # bfs 돌리기
    while Q:
        curX, curY = Q.popleft()
        for dir in range(8):
            nx = curX + dx[dir]
            ny = curY + dy[dir]
            if nx < 0 or nx >= N or ny < 0 or ny >= N: continue  # 범위 밖은 pass
            if board[nx][ny] != -1: continue  # 이미 방문한, dest가 -1이 아니면 pass
            if board[destX][destY] != -1: break  # 목표 지점을 방문했으면 (-1이 아니면) break
            # 방문하기
            board[nx][ny] = board[curX][curY] + 1
            Q.append((nx, ny))

    print(board[destX][destY])