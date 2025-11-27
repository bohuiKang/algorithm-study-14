from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]  # 0은 물에 잠김
max_safe_area_cnt = 1  # 최대 안전구역 개수

# board에서 max값 (가장 높은 높이) 찾기
max_height = 1
for i in range(N):
    for j in range(N):
        max_height = max(max_height, board[i][j])

# 물 잠기기
for water_height in range(1, max_height):
    # visited 초기화
    visited = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            # 물 높이보다 같거나 작은 건 0으로 만들기
            if 0 < board[i][j] <= water_height:
                board[i][j] = 0

    # bfs 시작점 잡기
    tmp_area_cnt = 0
    for i in range(N):
        for j in range(N):
            # 높이 값이 0이 아니면 물에 잠기지 않았으니까 bfs 돌리기 가능
            if board[i][j] > 0 and not visited[i][j]:
                Q = deque([(i, j)])
                tmp_area_cnt += 1  # 구역 +1 카운트 하기
                # bfs
                while Q:
                    curX, curY = Q.popleft()
                    for dir in range(4):
                        nx = curX + dx[dir]
                        ny = curY + dy[dir]
                        if nx < 0 or nx >= N or ny < 0 or ny >= N: continue  # 범위 밖은 pass
                        if board[nx][ny] == 0 or visited[nx][ny] == 1: continue  # 0이거나 이미 방문했으면 pass
                        # 방문하기
                        visited[nx][ny] = 1
                        Q.append((nx, ny))
    # bfs 다 돌면 max_safe_area_cnt 값 갱신
    max_safe_area_cnt = max(max_safe_area_cnt, tmp_area_cnt)

# 최대 안전구역 개수 구하기
print(max_safe_area_cnt)