# 1은 아직 온전한 치즈, 2는 곧 녹는 치즈
# 매시간마다 2는 0으로 0과 인접한 1은 2로 바꿈
from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def melt():
    visited = [[False] * M for _ in range(N)]
    q = deque([(0, 0)])
    visited[0][0] = True

    # 이번 시간에 녹는 치즈 개수
    melt_cnt = 0

    while q:
        r, c = q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                visited[nr][nc] = True
                if arr[nr][nc] == 0:
                    q.append((nr, nc))
                elif arr[nr][nc] == 1:
                    arr[nr][nc] = 2
                    melt_cnt += 1

    # 실제로 치즈 녹이기
    for r in range(N):
        for c in range(M):
            if arr[r][c] == 2:
                arr[r][c] = 0

    return melt_cnt

time = 0        # 걸린 시간
last = 0        # 마지막에 녹은 치즈 개수

while True:
    cnt = melt()
    if cnt == 0:       # 더 이상 녹을 치즈가 없으면 종료
        break
    last = cnt
    time += 1

print(time)
print(last)