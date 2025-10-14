n, m = map(int, input().split())  # n: 도시 크기, m: 선택할 치킨집 개수

# 도시 정보 입력
city = []
for i in range(n):
    city.append(list(map(int, input().split())))

# 집과 치킨집의 좌표를 저장
houses = []  # 집의 좌표들
chickens = []  # 치킨집의 좌표들

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            houses.append((i, j))  # 집 좌표 저장
        elif city[i][j] == 2:
            chickens.append((i, j))  # 치킨집 좌표 저장

def get_chicken_distance(house, chicken):
    """한 집과 치킨집 사이의 거리(맨해튼 거리) 계산"""
    return abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])

def get_city_chicken_distance(selected_chickens):
    """선택된 치킨집들에 대한 도시의 치킨 거리 계산"""
    total = 0
    for house in houses:
        # 각 집마다 가장 가까운 치킨집과의 거리를 구함
        min_dist = float('inf')
        for chicken in selected_chickens:
            dist = get_chicken_distance(house, chicken)
            min_dist = min(min_dist, dist)
        total += min_dist
    return total

def recur(arr, m, start=0, selected=[]):
    """재귀를 이용해 arr에서 m개를 선택하는 모든 조합 생성"""
    # 기저조건: m개를 모두 선택한 경우 현재 조합을 반환
    if len(selected) == m:
        return [selected[:]]
    
    result = []
    # start부터 끝까지 순회하며 조합 생성
    for i in range(start, len(arr)):
        selected.append(arr[i])
        result.extend(recur(arr, m, i + 1, selected))  # 다음 원소부터 재귀 호출
        selected.pop()
    
    return result

# 모든 치킨집 중에서 m개를 선택하는 조합을 시도
min_city_distance = float('inf')

# 재귀로 구현한 조합 함수를 사용하여 m개의 치킨집을 선택하는 모든 경우의 수 탐색
for selected in recur(chickens, m):
    # 현재 선택된 치킨집들로 도시의 치킨 거리 계산
    city_distance = get_city_chicken_distance(selected)
    # 최솟값 갱신
    min_city_distance = min(min_city_distance, city_distance)

# 결과 출력
print(min_city_distance)