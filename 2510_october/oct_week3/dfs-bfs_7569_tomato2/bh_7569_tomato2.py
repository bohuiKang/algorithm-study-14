from collections import deque

def bfs(q):
    global days, zero_tomato
    cnt = len(q)
    while q:
        # cnt 가 0이면 len(q) & days += 1
        if cnt == 0:
            cnt = len(q)
            days += 1

        th, tr, tc = q.popleft()
        cnt -= 1 # 익은 하나의 토마토에 대한 상하좌우 위아래

        for i in range(4):
            nr = tr + d[i][0]
            nc = tc + d[i][1]
            if 0 <= nr < N and 0 <= nc < M: # box 크기 범위를 벗어나지 않고
                if boxs[th][nr][nc] == 0: # 익지 않은 토마토일때
                    boxs[th][nr][nc] = 1 # 토마토를 익히고
                    zero_tomato -= 1 # 익은 토마토 제거하고
                    q.append((th, nr, nc)) # 좌표를 추가한다.

        for i in range(2):
            nh = th + d2[i]
            if 0 <= nh < H: # box 높이 범위를 벗어나지 않고
                if boxs[nh][tr][tc] == 0: # 익지 않은 토마토일때
                    boxs[nh][tr][tc] = 1 # 토마토를 익히고
                    zero_tomato -= 1 # 익은 토마토 제거하고
                    q.append((nh, tr, tc)) # 좌표를 추가한다.


M, N, H = map(int, input().split()) # 가로칸, 세로칸, 상자 개수  2 ≤ M,N ≤ 1,000
boxs = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)] # 1 익은 토마토, 0 익지 않은 토마토, -1 토마토가 없는 칸

d = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 상우하좌
d2 = (1, -1) # 위아래

days = 0
queue = deque()

zero_tomato = 0
for h in range(H):
    for r in range(N):
        for c in range(M):
            if boxs[h][r][c] == 1:
                queue.append((h, r, c))
            if boxs[h][r][c] == 0:
                zero_tomato += 1

bfs(queue)

if zero_tomato: # 안익은 토마토가 있으면
    print(-1)
else:
    print(days)

# print(boxs)