# bfs를 모든 1에서 동시실행
# bfs 시작지점은 1(일)으로 하고 연결된 인접정점은 기준정점 숫자 + 1로 해줌
# 모든 bfs가 끝나면 arr을 탐색해서 가장 높은수를 출력
# arr안에 0이 있으면 -1 출력 / 맨 처음부터 arr에 0이 없으면 0 출력
# 그래프 할당은 좌표튜플로

from collections import deque

M, N, H = map(int, input().split())  # 가로 M, 세로 N, 높이 H
arr = [list(list(map(int, input().split())) for _ in range(N)) for _ in range(H)]

# BFS 함수 구현
def BFS():
    q = deque()
    # 모든 익은 토마토를 동시에 큐에 넣음
    for h in range(H):
        for r in range(N):
            for c in range(M):
                if arr[h][r][c] == 1:
                    q.append((h, r, c))

    while q:
        h, r, c = q.popleft()
        for dh, dr, dc in [(0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1), (1, 0, 0), (-1, 0, 0)]:
            nh, nr, nc = h + dh, r + dr, c + dc
            if 0 <= nh < H and 0 <= nr < N and 0 <= nc < M and arr[nh][nr][nc] == 0:
                arr[nh][nr][nc] = arr[h][r][c] + 1
                q.append((nh, nr, nc))

# BFS 실행
BFS()

# 결과 계산
max_day = 0
has_zero = False
for height in arr:
    for row in height:
        for column in row:
            if column == 0:
                has_zero = True
            max_day = max(max_day, column)

if has_zero:
    print(-1)
elif max_day == 1:  # 처음부터 다 익은 경우
    print(0)
else:
    print(max_day - 1)