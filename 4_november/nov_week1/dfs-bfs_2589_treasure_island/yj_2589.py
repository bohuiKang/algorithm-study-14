from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 입력받기
height, width = map(int, input().split())
board = list(input() for _ in range(height))
ans_max_dist = 0

# 각각의 시작점에 대해 bfs 돌기
for i in range(height):
    for j in range(width):
        if board[i][j] == 'L':  # 육지(L)이면 시작점에 넣고 bfs 돌리기
            Q = deque([(i, j)])
            dist = [list([-1] * width) for _ in range(height)]  # 거리 board 초기화
            dist[i][j] = 0  # dist 거리 초기화
            tmp_max_dist = 0  # 최대 거리값 초기화
            # bfs
            while Q:
                curX, curY = Q.popleft()
                for dir in range(4):
                    nx = curX + dx[dir]
                    ny = curY + dy[dir]
                    if nx < 0 or nx >= height or ny < 0 or ny >= width: continue  # 범위 필터링
                    if dist[nx][ny] != -1 or board[nx][ny] == 'W': continue  # 이미 방문한 곳이거나 육지가 아니면 pass
                    dist[nx][ny] = dist[curX][curY] + 1  # 거리 시간 갱신
                    tmp_max_dist = max(tmp_max_dist, dist[nx][ny])  # max 거리값 갱신
                    Q.append((nx, ny))  # 큐에 다음 좌표 넣기
            # bfs 끝
            # bfs 끝나면 ans_max_dist 갱신하기
            ans_max_dist = max(ans_max_dist, tmp_max_dist)

print(ans_max_dist)