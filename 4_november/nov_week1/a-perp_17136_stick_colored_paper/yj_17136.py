board = [list(map(int, input().split())) for _ in range(10)]
papers = [0] * 6
min_total_papers = 25
total_papers = 0

def can_use_paper(x, y, num):  # 좌표, 탐색 범위
    """num*num 크기의 색종이를 붙일 수 있는지 확인하기"""
    for a in range(x, x + num):
        for b in range(y, y + num):
            # 범위 밖이거나 0이 있으면 4*4로 가기
            if a < 0 or a >= 10 or b < 0 or b >= 10: return False
            if board[a][b] == 0: return False
    # 모두 통과했으면 True 리턴
    return True

def to_zero(x, y, num):
    """색종이 붙이기 - 붙인 부분을 0으로 만들기"""
    for a in range(x, x + num):
        for b in range(y, y + num):
            board[a][b] = 0
    return

def to_one(x, y, num):
    """색종이 떼기 - 뗀 부분을 1로 만들기"""
    for a in range(x, x + num):
        for b in range(y, y + num):
            board[a][b] = 1
    return

def is_finished():
    """색종이 다 붙였는지 확인하는 함수"""
    for a in range(10):
        for b in range(10):
            if board[a][b] == 1:
                return False
    return True

def backtracking(total_papers):
    global min_total_papers
    # 기저조건
    if total_papers >= min_total_papers:
        return

    if is_finished():
        min_total_papers = min(min_total_papers, total_papers)
        return

    # 재귀파트
    for i in range(10):
        for j in range(10):
            if board[i][j] == 1:
                for num in range(5, 0, -1):
                    # 범위 check
                    if i + num < 10 and j + num < 10:
                        if papers[num] < 5 and can_use_paper(i, j, num):
                            to_zero(i, j, num)  # 1들을 0으로 변하게 하기
                            papers[num] += 1  # 해당 색종이 cnt + 1 하기
                            backtracking(total_papers + 1)  # 전체 사용 색종이 +1하기
                            # backtracking
                            to_one(i, j, num)
                            papers[num] -= 1

# for i in range(10):
#     for j in range(10):
#         if board[i][j] == 1:
#             # 5*5
#             if paper_5 < 5 and can_use_paper(i, j, 5):
#                 # 5*5 1들을 0으로 변하게 하기, 색종이5번 cnt+1 하기, 전체 사용 색종이 +1하기
#                 to_zero(i, j, 5)
#                 paper_5 += 1
#                 total_papers += 1

backtracking(0)

# 1이 남았으면 return -1
if min_total_papers == 25:  # 초기값 그대로 나오면 -1 출력하기
    print(-1)
else:
    print(min_total_papers)