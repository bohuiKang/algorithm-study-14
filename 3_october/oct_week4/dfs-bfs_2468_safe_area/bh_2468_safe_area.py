from collections import deque


def rainy(sr, sc, water):
    q = deque([(sr, sc)])
    while q:
        rr, cc = q.popleft()
        for dm, dn in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            dr = rr + dm
            dc = cc + dn
            if 0 <= dr < N and 0 <= dc < N:
                if area[dr][dc] > water and visited[dr][dc] == 0:
                    q.append((dr, dc))
                    visited[dr][dc] = 1
    return 1 # 하나의 영역 리턴


N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]
max_safe = 0
max_rainy = max(map(max, area))  # 지도 내 최대 높이

for i in range(0, max_rainy + 1): # 장마철 물의 양 1-max_rainy, 비 안옴 0
    result = 0
    visited = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if area[r][c] > i and visited[r][c] == 0:
                visited[r][c] = 1
                result += rainy(r, c, i)
    max_safe = max(max_safe, result)

print(max_safe)