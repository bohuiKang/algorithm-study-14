from collections import deque

M, N, H = map(int, input().split())

arr = [[list(map(int, input().split())) for _ in range(N)] for __ in range(H)]


dirs = [[1, 0], [0, -1], [-1, 0], [0, 1]] #상좌하우


def check_cant(): # 다 바꾼뒤에 못바꾼 토마토 있는지 확인 return이 -1이면 못바꾸는 것임
    ans = 1
    for h in range(H):
        for r in range(N):
            for c in range(M):
                if arr[h][r][c] == 0:
                    ans = -1
                    return ans
    return ans


def check_tomato(): # 토마토 좌표
    ans = 0
    tomato_list = []
    for h in range(H):
        for r in range(N):
            for c in range(M):
                if arr[h][r][c] == 1:
                    tomato_list.append((h, r, c, 0))
                elif arr[h][r][c] == 0:
                    ans = 1
    return ans, tomato_list



def bfs():
    day = 0
    ans, tomato_list = check_tomato() # ans == 0 이면 바꿀 익힐 토마토 없음
    if ans == 0:
        return day
    q = deque(tomato_list)

    time = 0
    while q:
        h, r, c, time = q.popleft()

        for dr, dc in dirs:
            nr = r + dr
            nc = c + dc

            if nr < 0 or nr >= N or nc < 0 or nc >= M or arr[h][nr][nc] != 0:
                continue
            arr[h][nr][nc] = 1
            q.append((h, nr, nc, time+1))
        # 위쪽
        if 0 <= h - 1 < H and arr[h-1][r][c] == 0 :
            arr[h-1][r][c] = 1
            q.append((h - 1, r, c, time+1))
        # 아래쪽
        if 0 <= h + 1 < H and arr[h+1][r][c] == 0 :
            arr[h+1][r][c] = 1
            q.append((h + 1, r, c, time + 1))

    day = time

    if check_cant() == -1:
        day = -1
        return day

    return day


print(bfs())

