from itertools import combinations
from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def check_s(com):
    s_cnt = 0

    for r, c in com:
        if arr[r][c] == "S":
            s_cnt += 1
        if s_cnt > 3:
            return True
    return False

def check_connecting(com):
    visited = set()
    q = deque([com[0]])
    visited.add(com[0])

    while q:
        r, c = q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            # 조합의 좌표가 com에 들어있고, 방문하지 않았을 경우
            if (nr, nc) in com and (nr, nc) not in visited:
                visited.add((nr, nc))
                q.append((nr, nc))

    # 방문한 곳의 개수가 7 -> 다 이어져 있을 경우만 출력
    return len(visited) == 7

arr = [list(input()) for _ in range(5)]
result_cnt = 0
coordinates = [(i, j) for i in range(5) for j in range(5)]

for com in combinations(coordinates, 7):
    if check_s(com) and check_connecting(com):
        result_cnt += 1

print(result_cnt)