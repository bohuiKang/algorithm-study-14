from collections import deque

import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
ddz = [1, -1]


def bfs():
    q = deque()

    # 처음에 익어있는 토마토 위치를 모두 큐에 넣음
    for i in range(H):
        for j in range(M):
            for k in range(N):
                if arr[i][j][k] == 1:
                    q.append((j, k, i))

    while q:
        # 현재 위치
        x, y, z = q.popleft()

        for d in range(4):
            # 인접한 위치
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < M and 0 <= ny < N and arr[z][nx][ny] == 0:
                arr[z][nx][ny] = arr[z][x][y] + 1  # 날짜 누적
                q.append((nx, ny, z))

        for dz in ddz:
            if 0 <= z + dz < H:
                if arr[z + dz][x][y] == 0:
                    arr[z + dz][x][y] = arr[z][x][y] + 1
                    q.append((x, y, z + dz))

    result = 0
    for layer in arr:
        for row in layer:
            # 익지 않은 토마토가 남아있는 경우 -1을 반환
            if 0 in row:
                return -1
        # 가장 마지막에 익은 토마토의 날짜
            result = max(result, max(row))

    # 1부터 시작했으니 -1
    return result - 1

N, M, H = map(int, input().split())
arr = []
for _ in range(H):
    arr.append([list(map(int, input().split())) for _ in range(M)])

print(bfs())