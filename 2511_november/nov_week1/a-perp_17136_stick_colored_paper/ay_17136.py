"""
1을 찾음
1을 찾고 size 5 -> 1로 줄이면서 맞는지 확인
맞으면 -> 해당 색종이 사용, (개수 1개차감)
색종이 개수가 모자라면 작은 size 색종이 사용

그리고 가능 size 부터 size 낮추면서 재귀 돌림
그 크기 이하는 들어갈수 있다는 거니까 다 돌려서 dfs 본다고 생각하면 됨
"""


paper = [list(map(int, input().split())) for _ in range(10)]
copy_paper = [row[:] for row in paper]
color_paper = {1: 5, 2:5, 3: 5, 4:5, 5:5}
min_cnt = 26

def left_paper_area(): # 남은 색종이 면적 구하기
    area = 0
    for i in range(1, 6):
        area += i * i * color_paper[i]
    return area


def find_next(r, c): # 다음 1 찾기
    # 1) 현재 행의 나머지 부분
    for nc in range(c, 10):
        if copy_paper[r][nc] == 1:
            return (r, nc)
    # 2) 다음 행들
    for nr in range(r+1, 10):
        for nc in range(10):
            if copy_paper[nr][nc] == 1:
                return (nr, nc)
    return None  # 더 이상 1이 없음

# 맞는 종이 찾기
def find_size(r, c, size):
    if r+size > 10 or c+size > 10:
        return 0
    for nr in range(r, r + size):
        for nc in range(c, c + size):
            if copy_paper[nr][nc] == 0:
                return 0 # size 맞지 않음
    return 1 # size 맞음


def cnt_paper(cnt, r, c, cnt_1):
    global min_cnt

    if cnt_1 == 0:  # 더이상 1이 남아있지 않으면
        min_cnt = min(cnt, min_cnt)
        return

    else: # 아직 1이 남아있으면 다음 1의 자리 찾아야함
        r, c = find_next(r, c)

    if cnt >= min_cnt: # 이미 찾은 더 작은 min_cnt랑 값 같아지면 종료
        return

    if cnt_1 > left_paper_area(): # 남은 색종이 면적 보다 종이에1 이 더 많으면 커버 못함
        return

    size = 5 # 종이 size 5부터 1까지 맞는 size 찾아서 덮기
    while size > 0:
        ans = find_size(r, c, size)
        if ans == 0: # size 맞지 않는 경우
            size -= 1
            continue
        else: # size가 맞으면
            while size > 0:
                if color_paper[size] == 0: # 해당 사이즈 개수 없으면 아래 사이즈로 변경
                    size -= 1
                else:
                    color_paper[size] -= 1
                    for nr in range(r, r+size):
                        for nc in range(c, c+size):
                            copy_paper[nr][nc] = 0

                    cnt_paper(cnt+1, r, c, cnt_1 - size * size)

                    for nr in range(r, r+size): # 원상복구 하는 부분
                        for nc in range(c, c+size):
                            copy_paper[nr][nc] = 1
                    color_paper[size] += 1
                    size -= 1 # 작은 사이즈도 확인 해봐야함


# 1인 영역 찾기
cnt_1 = 0

for r in range(10):
    for c in range(10):
        if copy_paper[r][c] == 1:
            cnt_1 += 1

cnt_paper(0, 0, 0, cnt_1)

if min_cnt == 26:
    min_cnt = -1
print(min_cnt)



"""
더 효율적인 코드 짜기 - feat.gpt
for 문으로 짜면 중첩으로 안써도 됨

for s in range(5, 0, -1):
    if color_paper[s] == 0:
        continue               # 재고 없으면 스킵 (placeable 검사 낭비 X)
    if not find_size(r, c, s):
        continue               # 배치 불가면 스킵

    # 배치
    color_paper[s] -= 1
    for nr in range(r, r+s):
        for nc in range(c, c+s):
            copy_paper[nr][nc] = 0

    cnt_paper(cnt+1, r, c, cnt_1 - s*s)

    # 복구
    for nr in range(r, r+s):
        for nc in range(c, c+s):
            copy_paper[nr][nc] = 1
    color_paper[s] += 1


 # 선택: 하한 가지치기
    # need_lb = (ones + 25 - 1) // 25
    # if cnt + need_lb >= min_cnt:
    #     return

"""