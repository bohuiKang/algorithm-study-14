from collections import deque

dc = [0, 1, 0, -1]
dr = [1, 0, -1, 0]

def bfs(sc, sr):
    global cnt
    q = deque()
    q.append([sc, sr])
    # 방문한 지역에 대해 arr에 -1 (방문표시)
    arr[sc][sr] = -1
    # 현재 q에 좌표가 이미 하나 들어갔으므로 temp(각 영역의 넓이)는 1부터 시작
    temp = 1

    while q:
        cc, cr = q.popleft()
        for i in range(4):
            nc = cc + dc[i]
            nr = cr + dr[i]
            if 0 <= nc < N and 0 <= nr < M and arr[nc][nr] == 0:
                arr[nc][nr] = -1
                q.append([nc, nr])
                temp += 1

    cnt += 1
    result.append(temp)

N, M, K = map(int, input().split())
arr = [[0] * M for _ in range(N)]
# cnt = 분리되어 나누어지는 영역의 개수
cnt = 0
result = []

for _ in range(K):
    r1, c1, r2, c2 = map(int, input().split())

    # 입력 받은 좌표를 이용해 해당 구역에 1씩 더해줌 -> 직사각형이 그려지지 않은 구역은 0이 됨
    for i in range(c1, c2):
        for j in range(r1, r2):
            arr[i][j] += 1


for i in range(N):
    for j in range(M):
        # 직사각형이 그려지지 않은 구역에 대해 영역 탐색
        if arr[i][j] == 0:
            bfs(i, j)

print(cnt)
print(*sorted(result))