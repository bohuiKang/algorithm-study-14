'''
별다른 특별한 로직이 없어보이니 완탐으로 진행
'''

from itertools import combinations
from collections import deque

dc = [0, 1, 0, -1]
dr = [1, 0, -1, 0]


def infection(temp):
    # deque에 virus 위치만 모아두었던 list를 다 넣어두고서 감염 진행
    q = deque(virus)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dc[i], y + dr[i]
            if 0 <= nx < N and 0 <= ny < M and temp[nx][ny] == 0:
                temp[nx][ny] = 2
                q.append((nx, ny))

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 초기 arr에서 비어있는 구역과 감염되어있는 구역을 각각 list에 저장해둠
empty = [(i, j) for i in range(N) for j in range(M) if arr[i][j] == 0]
virus = [(i, j) for i in range(N) for j in range(M) if arr[i][j] == 2]

answer = 0

# 세울 수 있는 3개의 벽의 위치에 대한 가능한 조합
for walls in combinations(empty, 3):
    # arr를 복사해옴
    temp = [row[:] for row in arr]
    # walls(현재 세울 3개의 벽의 위치 조합)의 x, y로 복사해둔 지도에 벽을 표시
    for x, y in walls:
        temp[x][y] = 1
    infection(temp)
    # 안전한 구역의 개수 = 각 줄에 남은 0의 개수의 총합
    safe = sum(row.count(0) for row in temp)
    answer = max(answer, safe)

print(answer)