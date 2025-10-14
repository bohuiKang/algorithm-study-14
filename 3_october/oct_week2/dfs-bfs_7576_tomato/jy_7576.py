'''
하루가 지날 때 마다 익은 토마토에 인접한(상하좌우에 있는) 토마토들이 익음
1 == 익은 토마토
0 == 익지 않은 토마토
-1 == 토마토가 들어있지 않음
'''
from collections import deque

import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs():
    q = deque()

    # 처음에 익어있는 토마토 위치를 모두 큐에 넣음
    for i in range(M):
        for j in range(N):
            if arr[i][j] == 1:
                q.append((i, j))

    while q:
        # 현재 위치
        x, y = q.popleft()

        for d in range(4):
            # 인접한 위치
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < M and 0 <= ny < N and arr[nx][ny] == 0:
                arr[nx][ny] = arr[x][y] + 1  # 날짜 누적
                q.append((nx, ny))

    result = 0
    for row in arr:
        # 익지 않은 토마토가 남아있는 경우 -1을 반환
        if 0 in row:
            return -1
        # 가장 마지막에 익은 토마토의 날짜
        result = max(result, max(row))

    # 1부터 시작했으니 -1
    return result - 1

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]

print(bfs())