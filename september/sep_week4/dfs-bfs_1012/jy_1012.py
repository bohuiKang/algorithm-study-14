dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def bfs():
    global cnt

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                arr[i][j] = -1
                q = [(i, j)]

                while q:
                    cc, cr = q.pop(0)

                    for k in range(4):
                        mc = cc + dc[k]
                        mr = cr + dr[k]

                        if 0 <= mc < N and 0 <= mr < M and arr[mc][mr] == 1:
                            arr[mc][mr] = -1
                            q.append((mc, mr))

                cnt += 1


T = int(input())

for tc in range(1, T+1):
    M, N, K = map(int, input().split())
    arr = [[0] * M for _ in range(N)]
    cnt = 0

    for k in range(K):
        r, c = map(int, input().split())
        arr[c][r] = 1

    bfs()
    print(cnt)