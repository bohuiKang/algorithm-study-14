from collections import deque


def bfs(q):
    time = 0

    while q:
        sr, sc = q.popleft()
        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nr = sr + dr
            nc = sc + dc
            if 0 <= nr < N and 0 <= nc < M and treasure_map[nr][nc] == 'L':
                if visited[nr][nc] == 0:
                    time = visited[sr][sc]
                    visited[nr][nc] = time + 1
                    q.append((nr, nc))
    return time

N, M = map(int, input().split())
treasure_map = list(input() for _ in range(N))
# 육지 L, 바다 W, 우회하지 않는 가장 긴 최단거리 양 끝에 보물이 있다.
# 이동 소요 시간은? 한칸 이동에 1시간.

max_time = 0
queue = deque()
for r in range(N):
    for c in range(M):
        if treasure_map[r][c] == 'L':
            visited = [[0] * M for _ in range(N)] # DP 방식으로
            queue.append((r, c))
            visited[r][c] = 1
            get_time = bfs(queue)
            max_time = max(max_time, get_time)
            # for row in visited: # DP 확인 로직
            #     print(*row)
            # print('--------------')

print(max_time)