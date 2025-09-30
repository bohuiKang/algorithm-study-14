from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

T = int(input())
for tc in range(1, T + 1):
    M, N, K = map(int, input().split())
    board = [[0] * M for _ in range(N)]

    # 입력받기
    for _ in range(K):
        y, x = map(int, input().split())
        board[x][y] = 1

    # bfs
    cnt = 0  # 구역 수
    visited = [[0] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if not visited[i][j] and board[i][j] == 1:  # 처음 방문하는데 지렁이가 있으면 -> 시작점이 i, j
                Q = deque([[i, j]])
                cnt += 1

                while Q:
                    curX, curY = Q.popleft()
                    for dir in range(4):
                        nx = curX + dx[dir]
                        ny = curY + dy[dir]
                        if nx < 0 or nx >= N or ny < 0 or ny >= M: continue  # 범위 밖이면 pass
                        if board[nx][ny] == 0 or visited[nx][ny] == 1: continue  # 벌레가 없거나 이미 방문했으면 pass
                        Q.append([nx, ny])
                        visited[nx][ny] = 1

    print(cnt)