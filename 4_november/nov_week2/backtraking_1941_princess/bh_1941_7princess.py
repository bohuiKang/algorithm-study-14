# 도연아 왜 싸우고 그래..
from itertools import combinations
from collections import deque

def bfs(lst):
    q = deque([(lst[0])])
    visited = {lst[0]} # set을 통해 중복을 없앤다.

    while q:
        m = q.popleft()
        r, c = m // 5, m % 5 # r은 나머지, c는 몫
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nr = r + dr
            nc = c + dc
            nxt = nr*5 + nc # 원래 lst의 값으로 보이게 변경
            if 0 <= nr < 5 and 0 <= nc < 5:
                if nxt in lst and nxt not in visited:
                    visited.add(nxt)
                    q.append(nxt)

    if len(visited) == 7:
        return 1
    else:
        return 0

# 입력
seat_chart = [input() for _ in range(5)]

ans = 0 # 칠공주 결성할 수 있는 모든 경우의 수
for comb in combinations(range(25), 7):
    Y = 0
    for co in comb:
        if seat_chart[co//5][co%5] == 'Y': # 위치값을 r, c로 계산한다.
            Y += 1
        if Y > 3: # 임도연파 학생 수가 4명 이상일 때
            break
    else: # 이다솜파 학생 수가 4명 이상일 때
        ans += bfs(comb)

print(ans)
