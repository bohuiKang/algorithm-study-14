paper = [list(map(int, input().split())) for _ in range(10)]
colored = [0, 5, 5, 5, 5, 5] # 1-5크기, 각 5장

def check_attach():
    pass

### 여기까지~~~



# 1을 발견하면 1부터 정사각형 확인
for r in range(10):
    for c in range(10):
        if paper[r][c] == 1:
            copy_p = [row[:] for row in paper]
            check_attach()

# 1	왼쪽 위에서부터 탐색 시작
# 2	1 발견 시 5x5부터 가능한 크기까지 시도
# 3	붙였다가 재귀 탐색 후 떼기 (백트래킹)
# 4	모든 1이 덮이면 최소 개수 갱신
# 5	불가능하면 -1 출력