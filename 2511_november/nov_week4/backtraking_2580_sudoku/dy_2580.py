lst = [list(map(int, input().split())) for _ in range(9)]
# 0 찾기
zero = [(i, j) for i in range(9) for j in range(9) if lst[i][j] == 0]


# 0을 찾으면 될 수 있는 후보군을 해당 자리에 넣는다.
# 후보군 찾는 함수
def can(x, y):
    c_lst = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    # 3*3 배열 시작점
    s, e = x // 3, y // 3

    for i in range(9):
        # discard, 인자값을 set에서 삭제, 삭제하려는 값이 set에 없어도 오류 발생 x
        # 가로 확인
        c_lst.discard(lst[x][i])
        # 세로 확인
        c_lst.discard(lst[i][y])
        # 3*3 배열 확인
    for r in range(s * 3, (s + 1) * 3):
        for c in range(e * 3, (e + 1) * 3):
            c_lst.discard(lst[r][c])
    return tuple(c_lst)


# 채워야하는 빈칸 개수
num = len(zero)
flag = False
def dfs(cnt):
    global flag
    if flag:
        return

    if cnt == num:
        flag = True
        for row in lst:
            print(*row)
        return

    r, c = zero[cnt]

    c_lst = can(r, c)

    # 후보 리스트가 비었다면 실패, return
    if not c_lst:
        return

    for cl in c_lst:
        lst[r][c] = cl
        dfs(cnt+1)
        # 재귀 종료 후 초기화
        lst[r][c] = 0
dfs(0)