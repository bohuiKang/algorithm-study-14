import sys
sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(10000)
dr = [-1, 1, 0, 0] # 상하좌우
dc = [0, 0, -1, 1] # 상하좌우

T = int(input())
for tc in range(1, T+1):
    M, N, K = map(int, input().split())
    # G = [[0]*M for _ in range(N)] # 밭 크기
    visited = [[1]*M for _ in range(N)] # 방문한 구역인지 확인 위해

    for i in range(K): # 배추 심기
        c, r = map(int, input().split())
        # G[r][c] = 1
        visited[r][c] = 0


    def dfs(r, c):
        visited[r][c] = 1 # 방문하면 1로 바꿈
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= N or nc < 0 or nc >= M or visited[nr][nc]: # 이미 방문했거나 인덱스 범위 넘으면 건너뜀
                continue
            # if G[nr][nc] == 1: # 배추 심어져 있으면
            dfs(nr,nc) # 새로 위치 이동하여 구역 찾기

    cnt = 0
    for r in range(N):
        for c in range(M):
            if visited[r][c]:
                continue
            dfs(r, c)
            cnt += 1

    print(cnt)