from itertools import combinations

# n: 도시의 크기 (n x n)
# m: 선택할 치킨집의 개수
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# 치킨집 위치 저장
chicken = []
# 치킨집 조합별 도시 치킨 거리 합
distance = []

# 도시를 순회하며 치킨집의 좌표를 찾아 리스트에 저장함
for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            chicken.append([i, j])

# 가능한 모든 치킨집 조합 생성
chicken = list(combinations(chicken, m))

# 특정 집에서 주어진 치킨집 조합 중 가장 가까운 거리 계산
# r1/c1 = 집 좌표, chicken = 치킨
def chi_dist(r1, c1, chicken):
    min_val = float('inf')
    for chi in chicken:
        r2, c2 = chi[0], chi[1]
        dist = abs(r1 - r2) + abs(c1 - c2)
        min_val = min(min_val, dist)  # 제일 짧은 값 구하기
    return min_val


# m개의 치킨집 조합중에서
for chi in chicken:
    # 현재 조합의 총 치킨 거리 합
    temp = 0
    # 모든집에 대하여
    for i in range(n):
        for j in range(n):
            # 집인 경우만
            if board[i][j] == 1:
                # 치킨거리구하기
                temp += chi_dist(i, j, chi)
    # 계산된 총 치킨 거리를 저장함
    distance.append(temp)

print(min(distance))