from collections import deque
delta = [(0,1), (0,-1), (1,0), (-1,0)]

T = int(input())
for _ in range(T):
    # 가로, 세로, 배추 개수
    m, n, k = map(int, input().split())
    # 밭 만들기
    lst = [[0]*n for _ in range(m)]
    # 배추 심기
    for _ in range(k):
        x, y = map(int, input().split())
        lst[x][y] = 1
    # 지렁이
    worm = 0
    for r in range(m):
        for c in range(n):
            # 배추 발견
            if lst[r][c] == 1:
                # 지렁이 한마리 추가
                worm += 1
                # 방문 예정에 현재 위치 추가
                stack = deque([(r, c)])
                # 방문 표시
                lst[r][c] = 0
                while stack:
                    # 방문
                    x, y = stack.pop()
                    # 상하좌우 방문 후 배추 발견시 방문 예정에 추가, 방문 표시
                    for i in range(4):
                        nr = x+delta[i][0]
                        nc = y+delta[i][1]
                        if 0 <= nr < m and 0 <= nc < n and lst[nr][nc] == 1:
                            stack.append((nr, nc))
                            lst[nr][nc] = 0
    print(worm)
