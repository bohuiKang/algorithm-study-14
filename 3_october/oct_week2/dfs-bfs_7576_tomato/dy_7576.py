'''
from collections import deque
def check_impossible():
    # 익어야하는 토마토의 수
    t = 0
    visited = [[0]*m for _ in range(n)]
    for r in range(n):
        for c in range(m):
            # 익지않았다면
            if lst[r][c] == 0:
                t += 1
                q = deque([(r, c)])
                visited[r][c] = 1
                #익은 토마토를 발견할때까지
                while q:
                    now_r, now_c = q.popleft()
                    for i in range(4):
                        nr, nc = now_r + delta[i][0], now_c + delta[i][1]
                        if 0 <= nr < n and 0 <= nc < m:
                            if lst[nr][nc] == 1:
                                break
                            elif visited[nr][nc] == 0 and lst[nr][nc] == 0:
                                q.append((nr, nc))
                                visited[nr][nc] = 1
                        if 0 <= nr < n and 0 <= nc < m and lst[nr][nc] == 1:
                            break
                else:
                    # 불가능
                    return -1

            elif lst[r][c] == 1:
                for i in range(4):
                    nr, nc = r + delta[i][0], c + delta[i][1]
                    if 0 <= nr < n and 0 <= nc < m:
                        if lst[nr][nc] != -1:
                            break
                else:
                    # 익은 토마토 주변이 모두 벽임
                    #빈 상자로 취급
                    lst[r][c] = -1
                    continue
                #익은 토마토 위치 추가
                tm.append((r,c))
    #익은 토마토 수
    tm_num = len(tm)
    #익어야하는 토마토가 없는 경우
    if t == 0:
        return 0
    #익어야하는 토마토는 있는데 익은 토마토가 아예 없는 경우
    elif tm_num == 0:
        return -1
    #모두 아니라면 토마토의 수 반환
    else:
        return t + tm_num

delta = [(0,1), (0,-1), (1,0), (-1,0)]

m, n = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]
# 익은 토마토의 위치
tm = []
tomato = check_impossible()
if tomato == -1:
    print(-1)
elif tomato == 0:
    print(0)
else:
    #날짜
    day = 0
    while tm:
        #새로 익은 토마토들의 위치
        tomorrow  = []
        for r, c in tm:
            for j in range(4):
                nr, nc = r + delta[j][0], c + delta[j][1]
                if 0 <= nr < n and 0 <= nc < m:
                    #익지 않은 토마토가 근처에 있다면
                    if lst[nr][nc] == 0:
                        #해당 토마토를 익음으로 갱신
                        lst[nr][nc] = 1
                        #새로 익은 토마토 위치 추가
                        tomorrow.append((nr, nc))
        #새로 익은 토마토의 위치리스트로 갱신
        tm = tomorrow
        #새로 익은 게 있을때
        if tm:
            # 날짜 갱신
            day += 1
    print(day)
'''
from collections import deque
delta = [(0,1), (0,-1), (1,0), (-1,0)]

m, n = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]

# bfs로 토마토 익히기
def bfs():
    q = deque()
    for r in range(n):
        for c in range(m):
            # 익힌 토마토가 있는 경우 위치와 날짜를 큐에 삽입
            if lst[r][c] == 1:
                q.append((r, c, 0))

    # 익혀진 토마토가 없는 경우 return 0
    if not q:
        return 0

    # 익혀진 토마토의 상하좌우 탐색
    while q:
        tr, tc, day = q.popleft()
        # 안익혀진 토마토 탐색
        for i in range(4):
            nr, nc = tr+delta[i][0], tc+delta[i][1]
            if 0 <= nr < n and 0 <= nc < m:
                # 있는 경우 익히고
                if lst[nr][nc] == 0:
                    lst[nr][nc] = 1
                    # 해당 토마토를 익힌 토마토의 날짜 + 1을 날짜로 할당, q에 삽입
                    q.append((nr, nc, day+1))
    # while이 종료된 후 day에는 맨 마지막 날이 할당되어있기에 현재 day = 최소 일수
    # 최소 일수 반환
    return day



# 안익은게 있는지 확인
def check():
    for r in range(n):
        for c in range(m):
            if lst[r][c] == 0:
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