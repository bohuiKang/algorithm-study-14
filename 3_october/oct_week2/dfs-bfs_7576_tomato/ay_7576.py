from collections import deque

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dirs = [[1, 0], [0, -1], [-1, 0], [0, 1]] #상좌하우
# def day_0 ():
#     ans = 1
#     for r in range(M):
#         for c in range(N):
#             if arr[r][c] == 0:
#                 ans = 0
#                 return ans
#     return ans


def check_cant(): # 다 바꾼뒤에 못바꾼 토마토 있는지 확인
    ans = 1
    for r in range(N):
        for c in range(M):
            if arr[r][c] == 0:
                ans = -1
                return ans
    return ans


def check_tomato(): # 토마토 좌표
    ans = 0
    tomato_list = []
    for r in range(N):
        for c in range(M):
            if arr[r][c] == 1:
                tomato_list.append((r, c, 0))
            elif arr[r][c] == 0:
                ans = 1
    return ans, tomato_list



def bfs():
    day = 0
    ans, tomato_list = check_tomato()
    if ans == 0:
        return day
    q = deque(tomato_list)

    time = 0
    while q:
        r, c, time = q.popleft()

        for dr, dc in dirs:
            nr = r + dr
            nc = c + dc

            if nr < 0 or nr >= N or nc < 0 or nc >= M or arr[nr][nc] != 0:
                continue
            arr[nr][nc] = 1
            q.append((nr, nc, time+1))

    day = time

    if check_cant() == -1:
        day = -1
        return day

    return day


print(bfs())

