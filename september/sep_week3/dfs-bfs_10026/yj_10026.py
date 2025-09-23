from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N = int(input())
board = [list(input()) for _ in range(N)]
RB_board = [[0] * N for _ in range(N)]  # R과 B가 같은 적록색약이 보는 board

# RB_board 생성
for a in range(N):
    for b in range(N):
        if board[a][b] == 'G':
            RB_board[a][b] = 'R'
        else:
            RB_board[a][b] = board[a][b]

def bfs(visited, cnt, board):  # 방문 배열, 구역의 수, 전체 그림 배열
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:  # 방문한 적 없으면
                # 시작 좌표 초기화
                q = deque([(i, j)])
                cnt += 1
                visited[i][j] = cnt
                while q:
                    curX, curY = q.popleft()
                    for dir in range(4):
                        nx = curX + dx[dir]
                        ny = curY + dy[dir]
                        if nx < 0 or nx >= N or ny < 0 or ny >= N: continue  # 범위 체크
                        if visited[nx][ny] != 0: continue  # 이미 방문한 곳이면 pass
                        if board[curX][curY] != board[nx][ny]: continue  # 색이 현재 좌표랑 다르면 pass
                        visited[nx][ny] = cnt
                        q.append((nx, ny))
    return cnt

# 일반인 bfs
visited = [[0] * N for _ in range(N)]
cnt = bfs(visited, 0, board)


# 적록색약 bfs (R == G) - 위에랑 똑같은 bfs 돌리기
visited_RG = [[0] * N for _ in range(N)]
cnt_RG = bfs(visited_RG, 0, RB_board)

print(cnt, cnt_RG)