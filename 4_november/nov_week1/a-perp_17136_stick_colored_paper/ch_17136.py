# 10x10 배열을 행우선순회로 모두탐색하며 1을 만나는 경우 매번 가능한 붙이는 경우중 제일 많이 1을 덮는 종이를 선택
# 이미 종이가 붙은 칸은 -1로 표시
# 가능한 붙이는 경우 : 종이가 범위를 벗어나거나 종이 구역안에 1이 없는 경우는 제외
# 색종이는 5개씩 가지고 있음

# 우,하 델타: 가지고 있는 종이 개수를 고려해서 최대 5까지
# 이후 각 델타단계에서 우,상 델타로 가운데 숫자들 1이 맞는지 탐색 
# (각 델타단계의 좌표까지 (i + dr*p, j + dr*p))
# - 1이 아닌 수를 만나면 break
# - 가능한 최대거리까지 가면 색칠시작

arr = [list(map(int, input().split())) for _ in range(10)]
# 각 종이 개수 카운팅리스트
left_paper = [0] + [5] * 5

def select_paper(start):
    i, j = start
    # 첫번째 델타 탐색 시작
    len_paper = float('inf')
    for dr, dc in [(1, 0), (0, 1)]:
        p = 1
        while p <= 5 and left_paper[p]:
            ni, nj = i + dr * p, j + dc * p
            if ni < 0 or ni >= 10 or nj < 0 or nj >= 10 or arr[ni][nj] != 1:
                break
            p += 1
            # 두번째 델타 탐색 시작(사각형 안쪽 부분)
            q = 1
            if dr == 1:
                while q <= p: 
                    xr, xc = (0, 1)
                    xi, xj = ni + xr * q, nj + xc * q
                    if xi < 0 or xi >= 10 or xj < 0 or xj >= 10 or arr[xi][xj] != 1:
                        break
                    q += 1
            else:
                while q <= p: 
                    xr, xc = (-1, 0)
                    xi, xj = ni + xr * q, nj + xc * q
                    if xi < 0 or xi >= 10 or xj < 0 or xj >= 10 or arr[xi][xj] != 1:
                        break
                    q += 1
            p = min(p, q)
        len_paper = min(len_paper, p)
        left_paper[p] -= 1
    # 가장 많은 1을 덮는 종이 붙이기
    for r in range(len_paper):
        for c in range(len_paper):
            arr[i + r][j + c] = -1

    
for i in range(10):
    for j in range(10):
        if arr[i][j] == 1:
            select_paper((i, j))
            
#########아직 풀이중인 코드#########