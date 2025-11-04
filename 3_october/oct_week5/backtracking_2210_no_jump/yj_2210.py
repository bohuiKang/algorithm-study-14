dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# dfs 방문 중복없이 돌리기
def dfs(curX, curY, number):  # 시작점 x좌표, y좌표, 시작점 위치의 숫자
    # 기저조건
    if len(number) == 6:
        if number not in ans_list:  # 중복 답이 아니면 ans_list에 담기
            ans_list.append(number)
        return

    for dir in range(4):
        nx = curX + dx[dir]
        ny = curY + dy[dir]
        if nx < 0 or nx >= 5 or ny < 0 or ny >= 5: continue  # 범위 밖이면 pass
        dfs(nx, ny, number + board[nx][ny])

board = [list(input().split()) for _ in range(5)]  # str로 받기
ans_list = []

# 모든 시작점에 대해 bfs 재귀
for i in range(5):
    for j in range(5):
        dfs(i, j, board[i][j])

print(len(ans_list))