# 바이러스 확산을 막기 위해 연구소에 벽을 세우자
# 연구소의 크기는 N*M
# 연구소는 빈칸 0, 벽 1, 바이러스 2 로 이루어져 있다.
# 바이러스는 상하좌우로 퍼진다.
# 새로 세울수 있는 벽의 개수는 딱 3개

from copy import deepcopy
from collections import deque

# 벽 위치 생성
def check_wall(start, path):

    if len(path) == 3:
        make_wall(path)
        return

    for i in range(start, len(empty_spot)):
        check_wall(i+1, path+[empty_spot[i]]) # 포함
        # check_wall(i+1, path) # 불포함


# 벽 세우기
def make_wall(path):
    global max_empty

    test_room = deepcopy(room)
    # 벽 세우기
    for i in range(3):
        rr, rc = path[i]
        test_room[rr][rc] = 1

    # 바이러스 위치 확인 및 확산
    for vr in range(N):
        for vc in range(M):
            if test_room[vr][vc] == 2:
                virus((vr, vc), test_room)

    # 바이러스 확산 후 빈칸 수 세기
    empty_cnt = calc_empty(test_room)
    max_empty = max(max_empty, empty_cnt)

# 바이러스 확산하기 => 복사본 사용
def virus(point, test_room):
    q = deque([point])
    while q:
        vr, vc = q.popleft()
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nr = vr + dr
            nc = vc + dc
            if 0 <= nr < N and 0 <= nc < M:
                if test_room[nr][nc] == 0:
                    test_room[nr][nc] = 2
                    q.append((nr, nc))

# 빈칸 수 세기
def calc_empty(test_room):
    cnt = 0
    for er in range(N):
        for ec in range(M):
            if test_room[er][ec] == 0:
                cnt += 1
    return cnt


# 입력
N, M = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
max_empty = 0

# 빈칸의 위치 저장
empty_spot = []
for r in range(N):
    for c in range(M):
        if room[r][c] == 0:
            empty_spot.append((r, c))

# 벽 위치 조합
check_wall(0, [])

print(max_empty)
