from collections import deque


def move(r, c, cnt, knight_r, knight_c):

    q = deque([(r, c, cnt)])
    chess[r][c] = 1 # 출발 위치 방문 표시

    while q:
        x, y, turn = q.popleft()

        if x == knight_r and y == knight_c: # 도착 위치와 비교
            return turn
        # 나이트가 갈 수 있는 8개 방향 모두 확인
        for dx, dy in [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2),(-1, -2)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < l and 0 <= ny < l and chess[nx][ny] == 0: # 범위를 벗어나지 않고 방문하지 않았으면,
                chess[nx][ny] = 1 # 방문 표시
                q.append((nx, ny, turn+1)) # 이동 횟수 증가시켜서 큐에 넣기


t = int(input())
for _ in range(t):
    l: int = int(input()) # 체스판 크기
    sx, sy = map(int, input().split()) # 나이트의 위치
    nr, nc = map(int, input().split()) # 나이트의 도착 위치
    chess = [[0] * l for _ in range(l)] # 나이트의 이동 확인

    if sx == nr and sy == nc: # 출발지와 도착지가 같을 때,
        print(0)
    else: # 출발지와 도착지가 다를 때,
        print(move(sx, sy, 0, nr, nc))