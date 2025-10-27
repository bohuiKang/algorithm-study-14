from collections import deque

dc = [0, 1, 0, -1]
dr = [1, 0, -1, 0]

def bfs(sc, sr):
    global cnt
    q = deque()
    q.append([sc, sr])
    arr[sc][sr] = -1
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
cnt = 0
result = []

for _ in range(K):
    r1, c1, r2, c2 = map(int, input().split())

    for i in range(c1, c2):
        for j in range(r1, r2):
            arr[i][j] += 1


for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            bfs(i, j)

print(cnt)
print(*sorted(result))