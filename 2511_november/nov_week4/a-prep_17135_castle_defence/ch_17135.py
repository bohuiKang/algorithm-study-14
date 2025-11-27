# 궁수 3명의 위치를 조합으로 정한다.
# 각 턴마다 BFS로 가장 가까운 적을 찾아서 제거한다.
# 공격이 끝나면 적을 한 칸씩 내린다. (맨 아래행은 사라짐)
# 모든 적이 없어질 때까지 반복하며 최대 처치 수를 구한다.

from collections import deque
from itertools import combinations
import copy

N, M, D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 궁수 위치에서 가장 가까운 적을 찾는 bfs
def BFS(start_col, board):
    # 시작은 격자판의 맨 아래행 (N-1, start_col)
    q = deque([(N - 1, start_col, 1)])     # (r, c, d)
    visited = [[0] * M for _ in range(N)]
    visited[N - 1][start_col] = 1   # 시작위치 방문처리

    # 좌, 상, 우 순서로 탐색
    dr = [0, -1, 0]
    dc = [-1, 0, 1]

    while q:
        r, c, d = q.popleft()
        if d > D:          # 사정거리 초과하면 건너뜀
            continue
        if board[r][c] == 1:
            return (r, c)  # 가장 가까운 적 좌표 반환
        for i in range(3):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                visited[nr][nc] = 1
                q.append((nr, nc, d + 1))
    return None  # 사정거리 내에 적이 없으면 None

# 적을 한 턴마다 한칸씩 내리는 함수 (맨 아래행은 사라지고 위에서 빈행 추가)
def move_enemies(board):
    board.pop()           # 맨 아래행 삭제
    return [[0] * M] + board     # 맨 위행 추가

# game: 게임을 진행하는 함수
def game(archers):
    board = copy.deepcopy(arr)
    total_kill = 0

    while sum(sum(row) for row in board) > 0:  # 적이 하나라도 남아있는 동안 반복
        targets = set()   # 이번 턴에 죽일 적들의 좌표 저장

        # 궁수 3명 각각 BFS 실행
        for col in archers:
            target = BFS(col, board)
            if target:
                targets.add(target)

        # 적 제거
        for r, c in targets:
            board[r][c] = 0
        total_kill += len(targets)

        # 적 한 칸 내리기
        board = move_enemies(board)

    return total_kill

# 궁수 3명 배치 조합 탐색
max_kill = 0
for archers in combinations(range(M), 3):
    kills = game(archers)
    max_kill = max(max_kill, kills)

print(max_kill)