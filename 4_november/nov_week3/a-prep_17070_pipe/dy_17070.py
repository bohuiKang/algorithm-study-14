from collections import deque

# 남의 코드 베껴왔습니다, 출처: https://nado-coding.tistory.com/27

# 집의 크기
n = int(input())
# 집의 상태
lst = [list(map(int, input().split())) for _ in range(n)]

# 3차원 dp, 3차원 방향을 넣는다.
# x,y 좌표, z가 방향
# dp[x][y][direction]: (x, y) 위치에서 direction 방향으로 놓인 파이프의 경우의 수
dp = [[[0] * 3 for _ in range(n)] for _ in range(n)]

# 초기 상태: (0, 1) 위치에 수평으로 놓인 파이프
dp[0][1][0] = 1

for x in range(n):
    for y in range(n):
        # 수평 방향
        if y + 1 < n and lst[x][y + 1] == 0:  # 오른쪽으로 이동 가능
            dp[x][y + 1][0] += dp[x][y][0]  # 수평 유지
        if x + 1 < n and y + 1 < n and lst[x + 1][y + 1] == 0 and lst[x][y + 1] == 0 and lst[x + 1][y] == 0:
            dp[x + 1][y + 1][2] += dp[x][y][0]  # 대각선으로 이동

        # 수직 방향
        if x + 1 < n and lst[x + 1][y] == 0:  # 아래로 이동 가능
            dp[x + 1][y][1] += dp[x][y][1]  # 수직 유지
        if x + 1 < n and y + 1 < n and lst[x + 1][y + 1] == 0 and lst[x][y + 1] == 0 and lst[x + 1][y] == 0:
            dp[x + 1][y + 1][2] += dp[x][y][1]  # 대각선으로 이동

        # 대각선 방향
        if y + 1 < n and lst[x][y + 1] == 0:  # 오른쪽으로 이동 가능
            dp[x][y + 1][0] += dp[x][y][2]  # 수평으로 이동
        if x + 1 < n and lst[x + 1][y] == 0:  # 아래로 이동 가능
            dp[x + 1][y][1] += dp[x][y][2]  # 수직으로 이동
        if x + 1 < n and y + 1 < n and lst[x + 1][y + 1] == 0 and lst[x][y + 1] == 0 and lst[x + 1][y] == 0:
            dp[x + 1][y + 1][2] += dp[x][y][2]  # 대각선으로 이동

# 결과 출력: (N-1, N-1) 위치에 도달하는 경우의 수
result = dp[n - 1][n - 1][0] + dp[n - 1][n - 1][1] + dp[n - 1][n - 1][2]
print(result)