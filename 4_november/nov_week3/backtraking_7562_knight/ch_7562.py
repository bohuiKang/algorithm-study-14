# 나이트가 이동 가능한 8칸을 델타로 구성
# bfs로 목표지점까지 모든 경우의 수를 탐색해 가장 빠른 경우 출력
# visited를 사용해 이미 방문한 칸은 가지 않도록 조정
from collections import deque
delta = [(2, 1), (1, 2), (-2, 1), (-1, 2), (2, -1), (1, -2), (-2, -1), (-1, -2)]

def bfs(N, sr, sc, tr, tc):
    # 시작과 도착이 같은 경우
    if sr == tr and sc == tc:
        return 0

    dist = [[-1] * N for _ in range(N)]
    dist[sr][sc] = 0

    q = deque([(sr, sc)])

    while q:
        r, c = q.popleft()

        # 목표 지점 도달
        if r == tr and c == tc:
            return dist[r][c]

        for dr, dc in delta:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr, nc))


T = int(input().strip())
for tc in range(T):
    N = int(input().strip())              # 체스판 한 변 길이
    sr, sc = map(int, input().split())   # 시작 좌표
    tr, tc = map(int, input().split())   # 목표 좌표

    print(bfs(N, sr, sc, tr, tc))
