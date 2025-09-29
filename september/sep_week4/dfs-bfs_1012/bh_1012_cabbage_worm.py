import sys; sys.stdin = open('input.txt', 'r')

dr, dc = [0, 1, 0, -1], [1, 0, -1, 0] # 우하좌상

def bfs(sr, sc):

    q = [(sr, sc)] # heap으로 저장된 좌표를 빼내어 1을 2로 변경
    while q:
        nr, nc = q.pop(0)
        # 이미 저장된 좌표를 다시 저장 가능, 다만 그 좌표를 확인할 때 값이 2면 continue
        if field[nr][nc] == 2:
            continue
        field[nr][nc] = 2 # 현재 배추 위치 값 변경

        for d in range(4):
            x = nr+dr[d]
            y = nc+dc[d]
            if 0 <= x < N and 0 <= y < M:
                if field[x][y] == 1:
                    q.append((x, y))

T = int(input())
for tc in range(1, T+1):
    M, N, K = map(int, input().split()) # 가로M 세로N 배추K개
    field = [[0]*M for _ in range(N)] # 배추 위치
    for i in range(K): # 배추 위치를 밭 arr에 표시
        c, r = map(int, input().split())
        field[r][c] = 1
    worm = 0 # 지렁이 수
    # 전체를 돌면서 1을 찾기 => 찾으면 좌표를 인자로 함수 호출
    for r in range(N):
        for c in range(M):
            if field[r][c] == 1:
                worm += 1
                bfs(r, c)

    print(worm)