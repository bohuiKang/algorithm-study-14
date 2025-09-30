# 유기농 배추
T = int(input())

def DFS(start):
    stack = [start]
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        for nxt in graph[node]:
            if nxt not in visited and arr[nxt[0]][nxt[1]] == 1:
                stack.append(nxt)

for tc in range(T):
    M, N, K = map(int, input().split())
    arr = [[0] * M for _ in range(N)]

    for i in range(K):
        x, y = map(int, input().split())
        arr[y][x] = 1

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    # 그래프 할당
    graph = {}
    for i in range(N):
        for j in range(M):
            for d in range(4):
                ni, nj = i + dr[d], j + dc[d]
                if 0 <= ni < N and 0 <= nj < M:
                    graph.setdefault((i, j), []).append((ni, nj))
                    graph.setdefault((ni, nj), []).append((i, j))

    visited = set()
    cnt = 0

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 and (i, j) not in visited:
                DFS((i, j))
                cnt += 1

    print(cnt)