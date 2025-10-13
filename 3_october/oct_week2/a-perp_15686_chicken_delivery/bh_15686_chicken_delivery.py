
def check_distance(sr, sc): # 치킨집 하나와 모든 집의 거리 합
    for dr in range(N):
        for dc in range(N):
            if city[dr][dc] == 1:
                chicken[idx][1] += abs(sr - dr) + abs(sc - dc)


def city_chicken_d(sr, sc): # 집에서 제일 가까운 치킨 거리
    distance = 0
    for dr in range(N):
        for dc in range(N):
            if city[dr][dc] == 1:
                pass

    return distance


N, M = map(int, input().split())
# 0 빈곳, 1 집, 2 치킨집
city = [list(map(int, input().split())) for _ in range(N)]
chicken = [[(),0] for _ in range(13)]

idx = 0
for r in range(N): # 치킨집을 기준으로 모든 집의 거리 합 저장
    for c in range(N):
        if city[r][c] == 2: # 치킨집이면,
            chicken[idx][0] = (r, c)
            check_distance(r, c) # 인덱스 번호 전달
            idx += 1 # 치킨 집의 개수 확인 가능

chicken.sort(key= lambda x: x[1], reverse=True)

for i in range(M-idx):  # 치킨집 폐업 시키기
    closed_r, closed_c = chicken[i][0]
    city[closed_r][closed_c] = 0

# # 순서 : 좌 상 우 하 좌하 좌상 우상 우하
# xy = [(0, -1), (-1, 0), (0, 1), (1, 0), (1, -1), (-1, -1), (-1, 1), (1, 1)]

chicken_distance = 0
for r in range(N): # 도시의 치킨 거리 구하기
    for c in range(N):
        if city[r][c] == 1: # 집이면,
            chicken_distance += city_chicken_d(r, c)

print(chicken_distance)