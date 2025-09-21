import sys; sys.stdin = open('input.txt','r')
from collections import deque

dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def bfs(sr, sc, color):
    queue = deque([(sr, sc)])

    while queue:
        nr, nc = queue.popleft()
        for d in range(4):
            dr = nr + dirs[d][0]
            dc = nc + dirs[d][1]
            if 0 <= dr < N and 0 <= dc < N:
                if visited[dr][dc]: # 방문했으면 패스
                    continue
                if arr[dr][dc] == color: # 색이 같으면 큐에 추가
                    visited[dr][dc] = 1 # 방문 처리
                    queue.append((dr, dc))
                    if arr[dr][dc] == 'G':  # 색약 확인을 위해 arr을 변경
                        arr[dr][dc] = 'R'

T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 그림의 크기 NxN
    arr = [list(map(str, input())) for _ in range(N)] # 그림 색깔 정보

    R_G = [0, 0] # R, RG(색약)

    visited = [[0] * N for _ in range(N)] # 색깔 확인 표시
    # no 색약 확인
    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                visited[r][c] = 1
                R_G[0] += 1
                bfs(r, c, arr[r][c])  # 위치, 색깔
                if arr[r][c] == 'G': # 색약 확인을 위해 arr을 변경
                    arr[r][c] = 'R'

    visited = [[0] * N for _ in range(N)]  # 색약 확인을 위한 초기화
    # 색약 확인
    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                visited[r][c] = 1
                R_G[1] += 1
                bfs(r, c, arr[r][c])  # 위치, 색깔

    print(*R_G)


# 1. bfs 안에 bfs를 호출해서 fail
'''
def bfs(color, queue):

    # 색약 체크를 위한 변수
    rc = ()
    nxt_q = deque([])

    while queue:
        nr, nc = queue.popleft()
        for d in range(4):
            dr = nr + dirs[d][0]
            dc = nc + dirs[d][1]
            if 0 <= dr < N and 0 <= dc < N:
                if visited[dr][dc]: # 방문했으면 패스
                    continue
                if arr[dr][dc] == color: # 색이 같으면 큐에 추가
                    visited[dr][dc] = 1 # 방문 처리
                    queue.append((dr, dc))
                # 색약 확인
                elif color == 'R' or color == 'G': # 색이 색약이면 bfs 재귀
                    if arr[dr][dc] == 'R' or arr[dr][dc] == 'G':
                        rc = (dr, dc)
                        nxt_q = deque([(dr, dc)]) # 큐 값을 새로 받기

    # 현재 큐의 while 문이 끝났을 때 새로운 bfs 함수 호출
    if nxt_q: # 색약 큐에 값이 있으면,
        cr, cc = rc
        visited[cr][cc] = 1 # 방문 처리
        R_G[0] += 1 # 색약 아닌 횟수 증가
        bfs(arr[cr][cc], nxt_q)

T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 그림의 크기 NxN
    arr = list(input() for _ in range(N)) # 그림 색깔 정보

    R_G = [0, 0] # R, RG(색약)
    visited = [[0] * N for _ in range(N)] # 색깔 확인 표시

    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                R_G[0] += 1
                R_G[1] += 1
                q = deque([(r, c)])
                bfs(arr[r][c], q) # 색깔, queue

    print(*R_G)
'''

# 2. 그냥 bfs와 색약 bfs 함수를 따로 만들어 pass 받음
# 코드가 길어서 싫음
'''
def bfs(sr, sc, color):
    queue = deque([(sr, sc)])

    while queue:
        nr, nc = queue.popleft()
        for d in range(4):
            dr = nr + dirs[d][0]
            dc = nc + dirs[d][1]
            if 0 <= dr < N and 0 <= dc < N:
                if visited[dr][dc]: # 방문했으면 패스
                    continue
                if arr[dr][dc] == color: # 색이 같으면 큐에 추가
                    visited[dr][dc] = 1 # 방문 처리
                    queue.append((dr, dc))


def bfs_gr(sr, sc, color): # 색약 bfs
    queue = deque([(sr, sc)])

    while queue:
        nr, nc = queue.popleft()
        for d in range(4):
            dr = nr + dirs[d][0]
            dc = nc + dirs[d][1]
            if 0 <= dr < N and 0 <= dc < N:
                if visited_gr[dr][dc]: # 방문했으면 패스
                    continue
                # 색약 색이면 큐에 추가
                if (color == 'R' or color == 'G') and (arr[dr][dc] == 'R' or arr[dr][dc] == 'G'):
                    visited_gr[dr][dc] = 1 # 방문 처리
                    queue.append((dr, dc))
                elif color == 'B' and arr[dr][dc] == color: # 색이 'B'인 경우
                    visited_gr[dr][dc] = 1 # 방문 처리
                    queue.append((dr, dc))

T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 그림의 크기 NxN
    arr = list(input() for _ in range(N)) # 그림 색깔 정보

    R_G = [0, 0] # R, RG(색약)
    visited = [[0] * N for _ in range(N)] # 색깔 확인 표시
    visited_gr = [[0] * N for _ in range(N)] # 색약 색깔 확인 표시

    for r in range(N):
        for c in range(N):
            if not visited[r][c]: # no 색약
                visited[r][c] = 1
                R_G[0] += 1
                bfs(r, c, arr[r][c])  # 위치, 색깔
            if not visited_gr[r][c]: # 색약
                visited_gr[r][c] = 1
                R_G[1] += 1
                bfs_gr(r, c, arr[r][c])  # 위치, 색깔

    print(*R_G)
'''