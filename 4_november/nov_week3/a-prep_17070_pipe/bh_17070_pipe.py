N = int(input()) # NxN
home = [list(map(int, input().split())) for _ in range(N)] # 빈칸 0, 벽 1

# 가로, 대각선, 세로(이동 가능)
# position = [[True, True, False], [True, True, True], [False, True, True]]
# move = [(0, 1), (1, 1), (1, 0)] # 오른쪽, 대각선, 아래 이동 좌표 및 빈칸 확인
# add_check = [(0, 1), (1, 0)] # 대각선 추가 확인
dp_visited = [[[0] * 3 for _ in range(N)] for _ in range(N)] # [r][c][방향]
dp_visited[0][1][0] = 1 # 출발 시점

end_ans = 0 # (N-1, N-1)까지 도착한 파이프 개수

for r in range(N):
    for c in range(2, N):
        if home[r][c] == 1:
            continue

        # 가로 방향 0 => 이전 방향이 가로 0 or 대각선 1
        # c 가 2부터 시작하므로 c-1 했을 때 인덱스 에러가 안나기에 조건문 사용 안함
        dp_visited[r][c][0] = dp_visited[r][c-1][0] + dp_visited[r][c-1][1]

        # 세로 방향 2 => 이전 방향이 세로 2 or 대각선 1
        # r(행) -1 을 하기에 인덱스 에러 방지를 위해 조건문 사용
        if r > 0:
            dp_visited[r][c][2] = dp_visited[r-1][c][2] + dp_visited[r-1][c][1]

        # 대각선 방향 1 => 이전 방향이 가로 0 or 세로 2 or 대각선 1
        # r-1,c-1 둘다 있기 때문에 조건문 사용
        if r > 0 and c > 0:
            # 대각선 이동의 경우 추가로 빈칸을 더 확인해야 함
            if home[r - 1][c] == 0 and home[r][c - 1] == 0:
                # 대각선 좌표에 저장   = 이전 가로 방향에서 대각선으로   + 이전 대각선 방향에서 대각선으로  + 이전 세로 방향에서 대각선으로
                dp_visited[r][c][1] = dp_visited[r - 1][c - 1][0] + dp_visited[r - 1][c - 1][1] + dp_visited[r - 1][c - 1][2]

# 3 방향 전체 도착 건수 합산
print(dp_visited[N-1][N-1][0]+dp_visited[N-1][N-1][1]+dp_visited[N-1][N-1][2])


## 시간초과 :)
# def move_pipe(r, c, pose):
#     global end_ans
#
#     if r == N-1 and c == N-1: # 끝까지 도착했다면,
#         end_ans += 1
#         return
#
#     for shape in range(3):
#         if position[pose][shape]: # shape => 0, 1, 2
#             for rr, cc in check_empty[shape]:
#                 nxt_r = r + rr
#                 nxt_c = c + cc
#
#                 if not(0 <= nxt_r < N and 0 <= nxt_c < N): # home 범위를 벗어 나거나,
#                     break
#                 elif home[nxt_r][nxt_c] == 1: # 벽이면,
#                     break
#             else:
#                 move_r = r + move[shape][0]
#                 move_c = c + move[shape][1]
#                 move_pipe(move_r, move_c, shape)
#
# N = int(input()) # NxN
# home = [list(map(int, input().split())) for _ in range(N)] # 빈칸 0, 벽 1
#
# # 가로, 대각선, 세로(이동 가능)
# position = [[True, True, False], [True, True, True], [False, True, True]]
# check_empty = [[(0, 1)], [(0, 1), (1, 0), (1, 1)], [(1, 0)]] # 오른쪽 이동을 위해, 대각선 이동을 위해, 아래 이동을 위해 => 확인할 빈칸
# move = [(0, 1), (1, 1), (1, 0)] # 오른쪽, 대각선, 아래 이동 좌표
# end_ans = 0 # (N-1, N-1)까지 도착한 파이프 개수
#
# ## 함수 호출
# move_pipe(0, 1, 0) # 시작(0, 1), 가로
#
# print(end_ans)