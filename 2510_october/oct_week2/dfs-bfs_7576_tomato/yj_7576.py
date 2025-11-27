from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

m, n = map(int, input().split())  # m: 가로(열)의 크기, n: 세로(행)의 크기

# 보드와 거리 배열 초기화
board = []  # 토마토 상태를 저장 (1: 익은 토마토, 0: 안 익은 토마토, -1: 빈 칸)
dist = []  # 각 위치까지 토마토가 익는 데 걸리는 일수

# BFS를 위한 큐 초기화
Q = deque()

# 입력 받으면서 초기 상태 설정
for i in range(n):
    r = list(map(int, input().split()))
    board.append(r)
    dist_row = []
    for j in range(m):
        if board[i][j] == 1:
            # 익은 토마토는 시작점이므로 큐에 추가
            Q.append((i, j))
            dist_row.append(0)  # 시작점의 거리는 0
        elif board[i][j] == 0:
            # 안 익은 토마토는 -1로 초기화 (아직 방문 안 함)
            dist_row.append(-1)
        else:  # board[i][j] == -1
            # 빈 칸은 0으로 설정 (방문할 필요 없음)
            dist_row.append(0)
    dist.append(dist_row)

# BFS 실행 (다중 시작점에서 동시에 퍼져나감)
while Q:
    cur_x, cur_y = Q.popleft()  # 현재 위치
    # 4방향(상하좌우)으로 탐색
    for dir in range(4):
        nx = cur_x + dx[dir]  # 다음 x 좌표
        ny = cur_y + dy[dir]  # 다음 y 좌표
        # 범위를 벗어나면 스킵
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        # 이미 방문했거나 빈 칸이면 스킵
        if dist[nx][ny] >= 0:
            continue
        # 거리 갱신: 현재 위치의 거리 + 1
        dist[nx][ny] = dist[cur_x][cur_y] + 1
        Q.append((nx, ny))  # 큐에 추가

# 결과 확인
ans = 0  # 토마토가 모두 익는 최소 일수
found_unripe = False  # 안 익은 토마토 발견 여부
for i in range(n):
    for j in range(m):
        if dist[i][j] == -1:  # 안 익은 토마토가 남아있으면
            print(-1)  # 모두 익지 못하는 상황
            found_unripe = True
            break
        # 가장 오래 걸린 시간이 전체 소요 시간
        ans = max(ans, dist[i][j])
    if found_unripe:
        break

# 모든 토마토가 익었으면 최소 일수 출력
if not found_unripe:
    print(ans)