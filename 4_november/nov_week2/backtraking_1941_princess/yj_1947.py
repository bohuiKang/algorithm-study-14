from itertools import combinations
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def is_connected(princesses):
    """ bfs 돌려서 서로 다 만나는지 확인"""
    # 초기화 - 첫 번째 공주 좌표부터 시작
    Q = deque([princesses[0]])
    visited = set()
    visited.add(princesses[0])
    while Q:
        curX, curY = Q.popleft()
        for dir in range(4):
            nx = curX + dx[dir]
            ny = curY + dy[dir]
            if nx < 0 or nx >= 5 or ny < 0 or ny >= 5: continue  # 범위 밖 pass
            if (nx, ny) not in princesses or (nx, ny) in visited: continue  # 칠공주 소속이 아니거나 방문했으면 pass
            visited.add((nx, ny))
            Q.append((nx, ny))
    return len(visited) == 7

board = list(input() for _ in range(5))

# 칠공주 조합 생성, (i, j) 좌표 형태로 저장
positions = [(i, j) for i in range(5) for j in range(5)]
answer = 0
for princesses in combinations(positions, 7):
    # 이다솜파가 4명 이상이 아니면 컷
    cntS = 0
    for pi, pj in princesses:
        if board[pi][pj] == 'S':
            cntS += 1
    if cntS < 4:
        continue

    # bfs 돌려서 서로 다 만나는지 확인
    if is_connected(princesses):
        answer += 1

print(answer)
