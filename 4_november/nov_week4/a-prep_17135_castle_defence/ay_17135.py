from collections import deque


# deque 도 인덱스 접근이 가능하지만 시간 복잡도가 더 높다고 ai 가 그럼

# 궁수 배치 조합 구하기 M 칸중 3칸 고르기 -> 궁수위치 [[N,c1], [N,c2], [N,c3]] -> (c1, c2, c3) -> deque에 담고 pop해서 진행

# 적위치를 담기 리스트에 [(r,c)]
# 적 위치와 궁수 위치 거리를 구함 for in 으로 그리고 가장 가까운 위치를 구하고 그 위치 인덱스도 구함
# 모든 궁수에 대해서 가장 짧은 거리의 적 구하고 -> 1이면 0으로 바꿈, cnt+1 하고  이미 0이면 continue
# 그리고 pop(idx)
# 남은 적 위치 c값 + 1
# 그리고 c+1 == N+1이 되면 멈추기 ->

# 초기 적위치 체크
def check_enemy_rc():
    enemy_list = []
    for r in range(N):
        for c in range(M):
            if grid[r][c] == 1:
                enemy_list.append((r, c))

    return enemy_list

# 궁수 위치 조합 구하기
def arr_rc():
    q = deque([])
    for c1 in range(M-2):
        for c2 in range(c1+1, M-1):
            for c3 in range(c2+1, M):
                q.append((c1, c2, c3))

    return q

# 최소 거리의 적 구하기
def cal_dist(c1, c2, c3, enemy_list):
    q = deque([])
    enemy_num = len(enemy_list)
    for c in [c1, c2, c3]:
        min_dist = float("inf")
        enemy_rc = 0

        for i in range(enemy_num):
            er, ec = enemy_list[i]
            dist = abs(er-N) + abs(ec-c)
            if min_dist > dist: # 최소 거리인 경우 적 위치를 담음
                min_dist = dist
                enemy_rc = (i, er, ec)
            elif min_dist == dist: # 같은 거리일 때 왼쪽이면 왼쪽 값 담음 열 비교함
                if enemy_rc[2] > ec:
                    enemy_rc = (i, er, ec)
        if min_dist <= D: # 그리고 최소 위치가 거리 제한 이하면 담음
            q.append(enemy_rc)

    return q

# 궁수가 적 공격하기, 최소 거리 적 구하기의 q가 들어간다.
def attack(q, enemy_list):
    cnt = 0
    while q:
        idx, er, ec = q.pop()
        if grid_copy[er][ec] == 1:
            cnt += 1
            grid_copy[er][ec] = 0
            enemy_list.remove((er, ec))

    return cnt, enemy_list

# 적 이동 이랑 끝까지 이동시 제거
def move_en(enemy_list):
    enemy_num = len(enemy_list)
    remove_list = deque([])
    for i in range(enemy_num):
        r, c = enemy_list[i]
        grid_copy[r][c] = 0
        enemy_list[i] = (r+1, c)
        if r+1 == N:
            remove_list.append((r+1, c))

    while remove_list:
        rc = remove_list.pop()
        enemy_list.remove(rc)
    for r, c in enemy_list:
        grid_copy[r][c] = 1

    return enemy_list

N, M, D = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(N)]


enemy_list = check_enemy_rc() # 초기 적 위치
arr_rc = arr_rc() # 초기 궁수 위치
cnt_max = 0
for c1, c2, c3 in arr_rc: # 궁수 조합에 따른 적 횟수 구하기
    grid_copy = [row[:] for row in grid]
    enemy_list_copy = enemy_list[:]
    cnt = 0
    while enemy_list_copy: # 게임 진행
        min_enemy_list = cal_dist(c1, c2, c3, enemy_list_copy)
        add_cnt, enemy_list_copy = attack(min_enemy_list, enemy_list_copy)
        cnt += add_cnt
        enemy_list_copy = move_en(enemy_list_copy)

    cnt_max = max(cnt, cnt_max)


print(cnt_max)