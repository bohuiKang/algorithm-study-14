from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def count_air():
    visited = [[False] * M for _ in range(N)]
    q = deque()
    # 시작점은 (0,0)으로 설정 -> 테두리는 항상 공기니까 이를 기점으로 0울 bfs 탐색
    q.append((0, 0))
    visited[0][0] = True

    while q:
        x, y = q.popleft()
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and board[nx][ny] == 0:
                    # 공기면 해당 칸을 True로 변경
                    visited[nx][ny] = True
                    q.append((nx, ny))
    return visited

# 그냥 치즈 세는거임
def count_cheese():
    cnt = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                cnt += 1
    return cnt

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

time = 0
prev_cheese = 0

while True:
    #현재 치즈 개수 세기
    cur_cheese = count_cheese()

    # 치즈가 0개 -> 걸린 시간 + 이전까지 있던 치즈 개수를 출력 후 함수 break
    if cur_cheese == 0:
        print(time)
        print(prev_cheese)
        break

    # 이전 치즈를 현재 치즈로 갱신
    prev_cheese = cur_cheese
    # 공기가 얼마나 있는지 세기
    outside = count_air()

    #녹아야 할 치즈의 좌표값을 저장
    melt = []
    for i in range(N):
        for j in range(M):
            # 치즈를 발견할 경우
            if board[i][j] == 1:
                for dir in range(4):
                    ni = i + dx[dir]
                    nj = j + dy[dir]
                    if 0 <= ni < N and 0 <= nj < M:
                        # 인접한 상하좌우 중 공기가 있을 경우 (=outside에서 해당 칸이 True일 경우)
                        if outside[ni][nj]:
                            # 녹아야 할 치즈로 추가
                            melt.append((i, j))
                            break

    # 치즈들을 녹임
    for x, y in melt:
        board[x][y] = 0

    # 시간을 추가
    time += 1