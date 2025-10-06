# 1. 이중 for문으로 시작점 잡고 bfs 돌리기
# 2. 단지개수 카운트
# 3. 단지별 집 수 리스트에 담기
# 4. 리스트 오름차순 정렬해서 출력
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N = int(input())
board = [list(map(int, input())) for _ in range(N)]
danji_cnt = 0   # 총 단지수
homes = []  # 단지내 집의 수
visited = [[0] * (N + 1) for _ in range(N)]

# 시작점 찾기
for i in range(N):
    for j in range(N):
        if board[i][j] == 1 and visited[i][j] == 0:
            danji_cnt += 1
            # 큐 초기화
            Q = deque([[i, j]])
            visited[i][j] = 1
            home_cnt = 1
            # bfs
            while Q:    # 큐가 빌때까지 bfs 돌기
                curX, curY = Q.popleft()
                for dir in range(4):
                    nx = curX + dx[dir]
                    ny = curY + dy[dir]
                    if nx < 0 or nx >= N or ny < 0 or ny >= N: continue  # 유효범위 체크
                    if board[nx][ny] == 0: continue   # 집이 없는 곳이면 pass
                    if visited[nx][ny] == 1: continue   # 이미 방문했던 곳이면 pass
                    visited[nx][ny] = 1     # 방문했다 표시
                    home_cnt += 1   # 집 세기
                    Q.append([nx, ny])  # 다음 방문점 큐에 넣기
            homes.append(home_cnt)
print(danji_cnt)
for home in sorted(homes):  # 오름차순으로 출력
    print(home)