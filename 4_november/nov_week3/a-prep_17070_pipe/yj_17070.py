N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

# dp[i][j][k] = (i,j) 위치에 k방향(0:가로, 1:세로, 2:대각선)으로 도착하는 경우의 수
dp = [[[0] * 3 for _ in range(N)] for _ in range(N)]

# 초기 상태: (0,1)에 가로 방향으로 1개
dp[0][1][0] = 1

# DP 계산
for i in range(N):  # 세로
    for j in range(N):  # 가로
        # 현재 칸이 벽이면 skip
        if board[i][j] == 1:
            continue

        # 가로 방향으로 도착 (이전: 가로 또는 대각선)
        if j > 0:
            dp[i][j][0] += dp[i][j-1][0]
            dp[i][j][0] += dp[i][j-1][2]

        # 세로 방향으로 도착 (이전: 세로 또는 대각선)
        if i > 0:
            dp[i][j][1] += dp[i-1][j][1]
            dp[i][j][1] += dp[i-1][j][2]

        # 대각선 방향으로 도착 (이전: 가로, 세로, 대각선 모두 가능)
        # 단, (i-1,j)와 (i,j-1)도 빈 칸이어야 함
        if i > 0 and j > 0:
            if board[i-1][j] == 0 and board[i][j-1] == 0:
                dp[i][j][2] += dp[i-1][j-1][0]
                dp[i][j][2] += dp[i-1][j-1][1]
                dp[i][j][2] += dp[i-1][j-1][2]

# (N-1, N-1)에 도착하는 모든 경우의 수 합산
answer = dp[N-1][N-1][0] + dp[N-1][N-1][1] + dp[N-1][N-1][2]
print(answer)