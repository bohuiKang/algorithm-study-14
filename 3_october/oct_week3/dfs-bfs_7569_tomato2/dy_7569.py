from collections import deque
delta = [(0,1), (0,-1), (1,0), (-1,0)]
updown = (-1, 1)

# 상자의 크기를 나타내는 두 정수 M,N과 쌓아올려지는 상자의 수를 나타내는 H
m, n, h = map(int, input().split())
lst = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

# bfs로 토마토 익히기
def bfs():
    q = deque()
    # 높이
    for d in range(h):
        # 행
        for r in range(n):
            # 열
            for c in range(m):
                # 익힌 토마토가 있는 경우 위치와 날짜를 큐에 삽입
                if lst[d][r][c] == 1:
                    q.append((d, r, c, 0))

    # 익혀진 토마토가 없는 경우 return 0
    if not q:
        return 0

    # 익혀진 토마토의 상하좌우 탐색
    while q:
        td, tr, tc, day = q.popleft()
        # 안익혀진 토마토 탐색
        for i in range(4):
            nr, nc = tr+delta[i][0], tc+delta[i][1]
            if 0 <= nr < n and 0 <= nc < m:
                # 있는 경우 익히고
                if lst[td][nr][nc] == 0:
                    lst[td][nr][nc] = 1
                    # 해당 토마토를 익힌 토마토의 날짜 + 1을 날짜로 할당, q에 삽입
                    q.append((td, nr, nc, day+1))
        # 위아래 탐색
        for j in range(2):
            nd = td+updown[j]
            #유효성 검정
            if 0<=nd<h:
                if lst[nd][tr][tc] == 0:
                    lst[nd][tr][tc] = 1
                    # 해당 토마토를 익힌 토마토의 날짜 + 1을 날짜로 할당, q에 삽입
                    q.append((nd, tr, tc, day+1))

    # while이 종료된 후 day에는 맨 마지막 날이 할당되어있기에 현재 day = 최소 일수
    # 최소 일수 반환
    return day



# 안익은게 있는지 확인
# 제발 들여쓰기 위치 좀
def check():
    for d in range(h):
        for r in range(n):
            for c in range(m):
                if lst[d][r][c] == 0:
                    return False
    return True

# 토마토를 익히고 최소 일수를 변수에 할당
day = bfs()
# 안익혀진 토마토가 있는지 확인
result = check()

# 안익혀진 토마토가 없다면
if result:
    print(day)
# 있다면
else:
    print(-1)