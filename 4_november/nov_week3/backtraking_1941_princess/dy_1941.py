'''
25개 칸 중 7개를 선택하는 모든 경우의 수
각 경우마다:
S가 4개 이상인지 체크
7개가 연결되어 있는지 BFS/DFS로 체크
'''
from itertools import combinations
from collections import deque
delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]


lst = [list(input()) for _ in range(5)]

# 연결되었는지, s가 4개 이상인지 확인하는 함수
def is_c(com):
    # s의 수를 카운트하는 변수
    s_num = 0
    # 리스트에 있는 좌표를 방문하였는지 세는 변수
    com_num = 0

    stack = deque()
    visited = [[True]*5 for _ in range(5)]
    sr, sc = com[0][0], com[0][1]
    stack.append((sr, sc))
    visited[sr][sc] = False
    if lst[sr][sc] == 'S':
        s_num += 1
    com_num += 1
    while stack:
        r, c = stack.pop()
        for i in range(4):
            nr = r + delta[i][0]
            nc = c + delta[i][1]
            if 0 <= nr < 5 and 0 <= nc < 5 and visited[nr][nc]:
                # com에 있는 좌표인지 확인
                if (nr, nc) in com:
                    # 있다면 s인지 확인 후 stack에 추가
                    if lst[nr][nc] == 'S':
                        s_num += 1
                    com_num += 1
                    stack.append((nr, nc))
                    visited[nr][nc] = False
    if s_num >= 4 and com_num == 7:
        return True
    else:
        return False


# 5x5의 모든 좌표의 리스트 생성
co = []
for r in range(5):
    for c in range(5):
        co.append((r, c))

cnt = 0
# 25개의 좌표 중 7개 선택
for com in combinations(co, 7):
    if is_c(com):
        cnt += 1
print(cnt)