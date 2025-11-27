from collections import deque

dx = [1, 0, -1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

M, N, H = map(int, input().split())
dist = [[[0 for _ in range(H)] for _ in range(M)] for _ in range(N)]  # 3차원 배열 0으로 초기화

Q = deque()  # BFS 큐 초기화

# 토마토 입력받기
for i in range(H):
    for j in range(N):
        row = list(map(int, input().split()))
        for k in range(M):
            dist[j][k][i] = row[k]  # board에 값 할당
            # 익은 토마토면 Q에 넣기 (여러 개의 시작점)
            if dist[j][k][i] == 1:
                Q.append((j, k, i))

# BFS
while Q:
    curX, curY, curZ = Q.popleft()
    for dir in range(6):
        nx = curX + dx[dir]
        ny = curY + dy[dir]
        nz = curZ + dz[dir]
        if nx < 0 or ny < 0 or nz < 0 or nx >= N or ny >= M or nz >= H: continue  # 범위 밖 pass
        if dist[nx][ny][nz] != 0: continue  # 익은 토마토거나 토마토 없는 곳이면 pass
        dist[nx][ny][nz] = dist[curX][curY][curZ] + 1
        Q.append((nx, ny, nz))

# max값 확인
day = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            # 안 익은 토마토가 있으면 exit
            if dist[j][k][i] == 0:
                print(-1)
                exit()

            # max 날짜 갱신
            if dist[j][k][i] > day:
                day = dist[j][k][i]

print(day - 1)  # 시작점이 1이니까 도착점은 -1 하기