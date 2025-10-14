def chicken_distance(start, survive):
    global answer

    # 선택된 M개의 치킨집과 집들 사이의 최소 거리 확인
    if len(survive) == M:
        total_d = 0
        for hr, hc in houses:
            distance = float('inf')
            for ckr, ckc in survive:
                calc = abs(ckr - hr) + abs(ckc - hc)
                distance = min(distance, calc)  # 집과 치킨의 최소 거리 선택
            total_d += distance
        answer = min(answer, total_d) # 도시의 치킨 거리가 제일 작은 값을 선택
        return

    # M 개만큼 치킨집을 선택
    for i in range(start, len(chickens)):
        chicken_distance(i+1, survive + [chickens[i]])


N, M = map(int, input().split())
# 0 빈곳, 1 집, 2 치킨집
city = [list(map(int, input().split())) for _ in range(N)]
houses = []
chickens = []

for r in range(N): # 치킨집을 기준으로 모든 집의 거리 합 저장
    for c in range(N):
        if city[r][c] == 1: # 집이면,
            houses.append((r, c))
        elif city[r][c] == 2: # 치킨이면,
            chickens.append((r, c))

answer = float('inf')
chicken_distance(0, [])
print(answer)



## 문제를 잘 읽자
# def check_distance(sr, sc, turn): # 치킨집 하나와 모든 집의 거리 합
#     global distance
#     for dr in range(N):
#         for dc in range(N):
#             if turn == 1: # 치킨 기준 집 찾기
#                 if city[dr][dc] == 1:
#                     chicken[idx][1] += abs(sr - dr) + abs(sc - dc)
#             else: # 집 기준 치킨 찾기
#                 if city[dr][dc] == 2:
#                     distance = min(distance, abs(sr - dr) + abs(sc - dc))
#                 if distance == 1:
#                     return
#
#
# N, M = map(int, input().split())
# # 0 빈곳, 1 집, 2 치킨집
# city = [list(map(int, input().split())) for _ in range(N)]
# chicken = [[(),0] for _ in range(13)]
#
# idx = 0
# for r in range(N): # 치킨집을 기준으로 모든 집의 거리 합 저장
#     for c in range(N):
#         if city[r][c] == 2: # 치킨집이면,
#             chicken[idx][0] = (r, c)
#             check_distance(r, c, 1) # 인덱스 번호 전달, 집을 찾는다.
#             idx += 1 # 치킨 집의 개수 확인 가능
#
# chicken.sort(key= lambda x: x[1], reverse=True)
#
# for i in range(idx-M):  # 치킨집 폐업 시키기
#     closed_r, closed_c = chicken[i][0]
#     city[closed_r][closed_c] = 0
#
# chicken_distance = 0
# for r in range(N): # 도시의 치킨 거리 구하기
#     for c in range(N):
#         if city[r][c] == 1: # 집이면,
#             distance = 10000*N # 재할당
#             check_distance(r, c, 2) # 인덱스 번호 전달, 치킨 집을 찾는다.
#             chicken_distance += distance
#
# print(chicken_distance)