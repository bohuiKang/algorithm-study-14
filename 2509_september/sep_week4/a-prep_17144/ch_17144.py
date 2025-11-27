# 죄송합니다 5번 틀리고 뭐가 틀린지 모르겠습니다.

N, M, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 공기청정기 위치 (두 행, 0번째 열)
cleaner = []
for i in range(N):
    if arr[i][0] == -1:
        cleaner.append(i)
up, down = cleaner[0], cleaner[1]

# 상하좌우 델타
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for _ in range(T):
    # 1. 먼지 확산
    temp = [[0] * M for _ in range(N)]
    temp[up][0] = -1
    temp[down][0] = -1

    for i in range(N):
        for j in range(M):
            if arr[i][j] > 0:
                dust = arr[i][j]
                spread = dust // 5
                cnt = 0
                # 4방향 확산
                for d in range(4):
                    ni, nj = i + dr[d], j + dc[d]
                    if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != -1:
                        temp[ni][nj] += spread
                        cnt += 1
                temp[i][j] += dust - spread * cnt
    arr = temp  # 확산 결과 반영

    # 2. 공기청정기 가동
    # 위쪽 (반시계) 
    for i in range(up - 1, 0, -1): arr[i][0] = arr[i - 1][0]        # 하
    for i in range(M - 1): arr[0][i] = arr[0][i + 1]                # 좌
    for i in range(up): arr[i][M - 1] = arr[i + 1][M - 1]           # 상
    for i in range(M - 1, 1, -1): arr[up][i] = arr[up][i - 1]       # 우
    arr[up][1] = 0

    # 아래쪽 (시계)
    for i in range(down + 1, N): arr[i - 1][M - 1] = arr[i][M - 1]  # 하
    for i in range(M - 1): arr[N - 1][i] = arr[N - 1][i + 1]        # 좌
    for i in range(N - 2, down - 1, -1): arr[i + 1][0] = arr[i][0]  # 상
    for i in range(M - 1, 1, -1): arr[down][i] = arr[down][i - 1]   # 우
    arr[down][1] = 0
                                      

# 3. 남은 먼지 계산
result = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] > 0:
            result += arr[i][j]

print(result)