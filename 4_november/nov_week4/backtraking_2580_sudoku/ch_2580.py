board = [list(map(int, input().split())) for _ in range(9)]

# 빈 칸들 저장
blanks = []
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            blanks.append((i, j))

# 빈칸 좌표에 num을 놓을 수 있는지 검사
def num_check(r, c, num):
    # 행 검사
    for j in range(9):
        if board[r][j] == num:
            return False

    # 열 검사
    for i in range(9):
        if board[i][c] == num:
            return False

    # 3x3 박스 검사
    sr = (r // 3) * 3  # 시작 행
    sc = (c // 3) * 3  # 시작 열
    for i in range(sr, sr + 3):
        for j in range(sc, sc + 3):
            if board[i][j] == num:
                return False

    return True

def dfs(idx):
    # 모든 빈 칸을 다 채웠으면 출력 후 종료
    if idx == len(blanks):
        for row in board:
            print(*row)

    r, c = blanks[idx]

    # 1 ~ 9까지 넣어보면서 검사
    for num in range(1, 10):
        if num_check(r, c, num):
            board[r][c] = num
            dfs(idx + 1)
            board[r][c] = 0  # 원복

dfs(0)