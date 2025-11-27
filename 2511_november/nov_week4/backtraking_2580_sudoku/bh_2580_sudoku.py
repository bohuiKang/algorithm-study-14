def get_possible_num(idx): # 빈칸에 들어갈 수 있는 수를 찾는 함수

    if idx == len(empty_arr): # idx가 끝까지 갔으면 모든 빈칸을 알맞게 채웠다는 뜻
        for row in sudoku:
            print(*row)
        return True # True를 반환함으로 이후의 재귀함수 호출들을 종료

    x, y = empty_arr[idx]
    box_idx = get_box_idx(x, y)

    # 숫자 1-9를 하나씩 가능한지 확인
    for num in range(1, 10):
        if not row_used[x][num] and not col_used[y][num] and not box_used[box_idx][num]:
            sudoku[x][y] = num # 스도쿠 판에 값 입력
            row_used[x][num] = True
            col_used[y][num] = True
            box_used[box_idx][num] = True
            if get_possible_num(idx + 1): # 다음 빈 좌표의 인덱스 값 넣고 재귀 시작
                return True # 이번 재귀 호출에서 해를 찾았다면 이후 재귀 호출을 모두 종료
            sudoku[x][y] = 0 # 백트래킹 (다시 빈 칸으로 돌려 놓음)
            row_used[x][num] = False
            col_used[y][num] = False
            box_used[box_idx][num] = False

def get_box_idx(i, j): # from_gemini
    """주어진 좌표가 속한 3x3 박스의 인덱스(0~8)를 반환"""
    # (r // 3) * 3 : 행 그룹 (0, 3, 6)
    # (c // 3) : 열 그룹 (0, 1, 2)
    return (i // 3) * 3 + (j // 3)

sudoku = [list(map(int, input().split())) for _ in range(9)] # 9x9
set_num_all = {i for i in range(1, 10)} # 1 ~ 9까지의 수를 가진 set

# --- 룩업 테이블 정의 (O(1) 검사를 위한 핵심) --- from gemini
# 각 행, 열, 3x3 박스에 1~9 숫자가 사용되었는지 기록
# 인덱스는 1부터 9까지의 숫자를 바로 쓰기 위해 크기 10으로 설정
row_used = [[False] * 10 for _ in range(9)]
col_used = [[False] * 10 for _ in range(9)]
box_used = [[False] * 10 for _ in range(9)]

empty_arr = [] # 빈칸의 좌표를 저장할 리스트
for r in range(9):
    for c in range(9):
        decimal = sudoku[r][c]
        if decimal == 0:
            empty_arr.append((r, c)) # 튜플로 빈칸의 좌표를 리스트에 저장
        else: # 빈칸이 아니면, 룩업 테이블의 값을 True로 변경
            box_idx = get_box_idx(r, c)
            row_used[r][decimal] = True
            col_used[c][decimal] = True
            box_used[box_idx][decimal] = True
            
get_possible_num(0) # 첫 번째 빈칸 부터 숫자 채우기 시작
