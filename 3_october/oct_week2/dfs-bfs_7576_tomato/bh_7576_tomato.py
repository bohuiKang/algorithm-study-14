from collections import deque

def bfs(q):
    global days, zero_tomato
    cnt = len(q)
    while q:
        # cnt 가 0이면 len(q) & days += 1
        if cnt == 0:
            cnt = len(q)
            days += 1

        tr, tc = q.popleft()
        cnt -= 1
        for i in range(4):
            nr = tr + d[i][0]
            nc = tc + d[i][1]
            if 0 <= nr < N and 0 <= nc < M: # box 범위를 벗어나지 않고
                if box[nr][nc] == 0: # 익지 않은 토마토일때
                    box[nr][nc] = 1 # 토마토를 익히고
                    zero_tomato -= 1 # 익은 토마토 제거하고
                    q.append((nr, nc)) # 좌표를 추가한다.


M, N = map(int, input().split()) # 가로칸, 세로칸. 2 ≤ M,N ≤ 1,000
box = [list(map(int, input().split())) for _ in range(N)] # 1 익은 토마토, 0 익지 않은 토마토, -1 토마토가 없는 칸

d = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 상우하좌

days = 0
queue = deque()

zero_tomato = 0
for r in range(N):
    for c in range(M):
        if box[r][c] == 1:
            queue.append((r, c))
        if box[r][c] == 0:
            zero_tomato += 1


bfs(queue)
if zero_tomato: # 안익은 토마토가 있으면
    print(-1)
else:
    print(days)