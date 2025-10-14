# bfs를 모든 1에서 동시실행
# bfs 시작지점은 1(일)으로 하고 연결된 인접정점은 기준정점 숫자 + 1로 해줌
# 모든 bfs가 끝나면 arr을 탐색해서 가장 높은수를 출력
# arr안에 0이 있으면 -1 출력 / 맨 처음부터 arr에 0이 없으면 0 출력
# 그래프 할당은 좌표튜플로

from collections import deque

M, N = map(int, input().split())  # 가로 M, 세로 N
arr = [list(map(int, input().split())) for _ in range(N)]

# 그래프를 좌표 튜플 기반 무향간선할당
# graph = {}
# for r in range(N):
#     for c in range(M):
#         for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#             nr, nc = r + dr, c + dc
#             if 0 <= nr < N and 0 <= nc < M:
#                 graph.setdefault((r, c), []).append((nr, nc))

# BFS 함수 정의
def bfs():
    q = deque()
    # 모든 익은 토마토를 동시에 큐에 넣음
    for r in range(N):
        for c in range(M):
            if arr[r][c] == 1:
                q.append((r, c))

    while q:
        r, c = q.popleft()
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0:
                arr[nr][nc] = arr[r][c] + 1
                q.append((nr, nc))

# BFS 실행
bfs()

# 결과 계산
max_day = 0
has_zero = False
for row in arr:
    for day in row:
        if day == 0:
            has_zero = True
        max_day = max(max_day, day)

if has_zero:
    print(-1)
elif max_day == 1:  # 처음부터 다 익은 경우
    print(0)
else:
    print(max_day - 1)