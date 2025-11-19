
N = int(input())

house_grid = [list(map(int, input().split())) for _ in range(N)] # 집 상태

memo = [[[-1]*4 for _ in range(N)] for _ in range(N)]
first_rc = (0,0,0,1)

pipe_move = {
    1 : [(0, 1, 0, 1), (0, 1, 1, 1)], # 가로
    2 : [(1, 0, 1, 0), (1, 0, 1, 1)], # 세로
    3 : [(1, 1, 0, 1), (1, 1, 1, 0), (1, 1, 1, 1)], # 대각선
}
block = {
    1 : [(0, 1)],
    2 : [(1, 0)],
    3 : [(0, 1), (1, 0), (1, 1)]

}

def pipe_way(r1, c1, r2, c2): # 파이프가 놓인 방향
    if r2-r1 == 0:
        return 1
    elif c2-c1 == 0:
        return 2
    else:
        return 3

def block_way(dr2, dc2): # 파이프 이동시 주변 확인해야 하는 벽 위치
    if dr2 == 0:
        return 1
    if dc2 == 0:
        return 2
    else:
        return 3


def dfs(r1, c1, r2, c2):
    if r2 == N-1 and c2 == N-1:
        return 1
    way = pipe_way(r1, c1, r2, c2) # 파이프 놓인 방향 key 값 반환

    if memo[r2][c2][way] != -1:
        return memo[r2][c2][way]

    total = 0

    for dr1, dc1, dr2, dc2 in pipe_move[way]: # 파이프 이동 방향 호출
        nr1, nc1, nr2, nc2 = r1+dr1, c1+dc1, r2+dr2, c2+dc2

        if nr2 < 0 or nr2 >= N or nc2 < 0 or nc2 >= N: # 범위 벗어났는지 확인하는 if 문
            continue

        blocks = block[block_way(dr2, dc2)] # 벽있는지 확인해야  하는 위치
        for dr, dc in blocks: # 벽인지 확인하는 for 문
            nr, nc = r2 + dr , c2 + dc
            if house_grid[nr][nc]: # 벽이 있으면 그 방향으로 이동 못하므로 break 하고
                break
        if house_grid[nr][nc]: # continue로 넘김
            continue

        total += dfs(nr1, nc1, nr2, nc2)

    memo[r2][c2][way] = total
    return total

r1, c1, r2, c2 = first_rc
print(dfs(r1, c1, r2, c2))



# def dfs(r1, c1, r2, c2):
#     global cnt
#     q = deque([(r1, c1, r2, c2)])
#
#     while q:
#         r1, c1, r2, c2 = q.pop()
#         if r2 == N - 1 and c2 == N - 1:
#             cnt += 1
#             continue
#         way = pipe_way(r1, c1, r2, c2) # 파이프 놓인 방향 key 값 반환
#         for dr1, dc1, dr2, dc2 in pipe_move[way]:  # 파이프 이동 방향 호출
#             nr1, nc1, nr2, nc2 = r1 + dr1, c1 + dc1, r2 + dr2, c2 + dc2
#
#             if nr2 < 0 or nr2 >= N or nc2 < 0 or nc2 >= N:  # 범위 벗어났는지 확인하는 if 문
#                 continue
#
#             blocks = block[block_way(dr2, dc2)]  # 벽있는지 확인해야  하는 위치
#             for dr, dc in blocks:  # 벽인지 확인하는 for 문
#                 nr, nc = r2 + dr, c2 + dc
#                 if house_grid[nr][nc]:  # 벽이 있으면 그 방향으로 이동 못하므로 break 하고
#                     break
#             if house_grid[nr][nc]:  # continue로 넘김
#                 continue
#
#             q.append((nr1, nc1, nr2, nc2))

