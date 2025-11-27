from itertools import combinations
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())
origin_board = [list(map(int, input().split())) for _ in range(N)]
ans = -1

# 1. 3중 for문으로 벽 3개 세우기
# 빈 칸의 좌표를 1차원 리스트에 모두 모으기
comb_lst = []  # combination 돌릴 리스트
for i in range(N):
    for j in range(M):
        if origin_board[i][j] == 0:
            comb_lst.append((i, j))

# combination으로 3개 뽑아서 큐에 넣기, 이 세 개는 벽(1)로 바꾸기
for x in combinations(comb_lst, 3):
    # origin_board 복사본 board 만들기
    board = [row[:] for row in origin_board]

    # 벽 세 개를 세우기
    for a1, a2 in x:
        board[a1][a2] = 1

    # 2. 모든 바이러스를 큐에 넣고 bfs 돌리기
    Q = deque([])  # 바이러스를 큐에 bfs 시작점으로 넣는다.
    for i in range(N):
        for j in range(M):
            if board[i][j] == 2:
                Q.append((i, j))

    while Q:
        curX, curY = Q.popleft()
        for dir in range(4):
            nx = curX + dx[dir]
            ny = curY + dy[dir]
            if nx < 0 or nx >= N or ny < 0 or ny >= M: continue  # 범위 밖이면 pass
            if board[nx][ny] != 0: continue  # 빈 공간(0)이 아니면 pass
            board[nx][ny] = 2  # 바이러스 퍼짐
            Q.append((nx, ny))  # 큐에 퍼진 바이러스 위치 넣기

    # 3. bfs 끝나고 남은 0들을 카운트해서 출력한다.
    cnt = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                cnt += 1

    # 4. 안전 영역 크기의 최댓값을 갱신한다.
    ans = max(ans, cnt)

print(ans)