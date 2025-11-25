from collections import deque

# 기사(x, y)가 갈 수 있는 곳
# (x-1, y-2), (x-2, y-1), (x-2, y+1), (x-1, y+2), (x+1, y-2), (x+2, y-1), (x+1, y+2), (x+2, y+1)
direction = [(-1, -2), (-2, -1), (-2, +1), (-1, +2), (+1, -2), (+2, -1), (+1, +2), (+2, +1)]


# 최소이동 횟수기에  bfs
def bfs(sr, sc, er, ec):
    # 출발지와 도착지가 같다면 이동횟수 0 반환
    if sr == er and sc == ec:
        return 0

    # 현재 위치 큐에 넣고 시작 (r, c, 이동횟수)
    q = deque([(sr, sc, 0)])
    # 방문 목록에 표시
    visited = [[True] * l for _ in range(l)]
    visited[sr][sc] = False
    # bfs 시작
    while q:
        r, c, n = q.popleft()
        for i in range(8):
            nr, nc = r + direction[i][0], c + direction[i][1]
            # 유효성 검증
            if 0 <= nr < l and 0 <= nc < l and visited[nr][nc]:
                # 원하는 곳이 맞는지 확인
                if nr == er and nc == ec:
                    # 맞다면 이동횟수 반환
                    return n + 1
                # 아니라면 큐에 추가하여 이동
                q.append((nr, nc, n + 1))
                visited[nr][nc] = False


# 테스트 케이스
tc = int(input())
for t in range(tc):
    # 체스판의 한 변의 길이
    l = int(input())
    # 현재위치
    s_r, s_c = map(int, input().split())
    # 이동하려는 칸
    e_r, e_c = map(int, input().split())
    print(bfs(s_r, s_c, e_r, e_c))
