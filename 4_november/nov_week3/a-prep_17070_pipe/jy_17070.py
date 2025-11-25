N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[[0] * 3 for _ in range(N)] for _ in range(N)]
# (0,1)부터 시작하는 상황
# (0,1)까지 오는 방법은 하나밖에 없으니까 dp[0][1][0] = 1
# dp[x][y][z] : x, y = 좌표, z = 방향 (0: 가로, 1: 세로, 2: 가로)
dp[0][1][0] = 1

for r in range(N):
    # 이미 파이프가 (0,1) 에 위치하고 있으므로 c의 범위는 2부터 시작
    for c in range(2, N):
        # 칸이 이미 채워져있을 경우에는 continue
        if arr[r][c] == 1:
            continue

        # 가로
        dp[r][c][0] = dp[r][c - 1][0] + dp[r][c - 1][2]

        # 세로
        # 세로로 파이프가 존재하기 위해서는 r이 최소 1이어야 함
        if r > 0:
            dp[r][c][1] = dp[r - 1][c][1] + dp[r - 1][c][2]

        # 대각선
        # 세로의 조건과 더불어 가로 세로로 인접한 칸들 또한 비어있어야 함
        if r > 0 and arr[r][c - 1] == 0 and arr[r - 1][c] == 0:
            dp[r][c][2] = dp[r - 1][c - 1][0] + dp[r - 1][c - 1][1] + dp[r - 1][c - 1][2]

result = 0
# 각 방향의 배열 한쪽 끝 값을 저장
for i in range(3):
    result += dp[N - 1][N - 1][i]

print(result)
