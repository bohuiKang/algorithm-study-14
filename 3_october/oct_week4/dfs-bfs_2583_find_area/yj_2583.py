from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

M, N, K = map(int, input().split())  # 모눈종이 크기 N, M, 직사각형 개수 K
board = [[0] * N for _ in range(M)]  # 0으로 초기화
ans_list = []

# 1. 직사각형 좌표 입력에 따라 board를 1로 채우기
for k in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):  # [0, 1, 2, 3]
        for y in range(y1, y2):  # [2, 3]
            board[y][x] = 1

# 2. bfs
# 2중 for문으로 bfs 돌릴 첫 좌표를 찾기
for i in range(M):
    for j in range(N):
        if board[i][j] == 0:
            Q = deque([(i, j)])  # 첫 좌표 찾음
            board[i][j] = 1  # 첫 좌표 방문
            area = 1  # 분리된 영역 초기화
            # bfs 돌리기
            while Q:
                curX, curY = Q.popleft()
                for dir in range(4):
                    nx = curX + dx[dir]
                    ny = curY + dy[dir]
                    if nx < 0 or nx >= M or ny < 0 or ny >= N: continue  # 범위 밖이면 pass
                    if board[nx][ny] == 1: continue  # 직사각형이거나 이미 방문한 곳이면 pass
                    board[nx][ny] = 1  # 방문하기
                    Q.append((nx, ny))  # 다음 방문할 큐에 넣기
                    area += 1  # 분리된 영역 + 1 하기
            # bfs 끝나면 ans_list에 area 담기
            ans_list.append(area)

# 3. ans_list 오름차순 정렬해서 출력
ans_list.sort()
print(len(ans_list))
print(*ans_list)