# 참외밭
'''
입력: 첫 번째 줄에 1m2의 넓이에 자라는 참외의 개수를 나타내는 양의 정수 K (1 ≤ K ≤ 20)가 주어진다. 
참외밭을 나타내는 육각형의 임의의 한 꼭짓점에서 출발하여 반시계방향으로 둘레를 돌면서 
지나는 변의 방향과 길이 (1 이상 500 이하의 정수) 가 둘째 줄부터 일곱 번째 줄까지 한 줄에 하나씩 순서대로 주어진다. 
변의 방향에서 동쪽은 1, 서쪽은 2, 남쪽은 3, 북쪽은 4로 나타낸다.
7
4 50
2 160
3 30
1 60
3 20
1 100

7
1 10
4 60
2 60
3 30
1 50
3 30

출력: 첫째 줄에 입력으로 주어진 밭에서 자라는 참외의 수를 출력한다.
47600
'''
# 1m^2당 참외 수
korean_melon = int(input())
land = [list(map(int, input().split())) for _ in range(6)]

# 가로 / 세로 중 가장 큰 값의 인덱스 저장 변수
width_max_idx = 0 if land[0][0] == 1 or land[0][0] == 2 else 1 # 가로의 인덱스로 시작
length_max_idx = 0 if land[0][0] == 3 or land[0][0] == 4 else 1 # 세로의 인덱스로 시작

for i in range(6):
    if land[i][0] == 1 or land[i][0] == 2 : # 가로
        if land[width_max_idx][1] < land[i][1]:
            width_max_idx = i
    else: # 세로
        if land[length_max_idx][1] < land[i][1]:
            length_max_idx = i

## 제거할 땅 크기 1
# small_w = 0
# small_h = 0
# if width_max_idx+1 == length_max_idx: # width -> length 순서
#     small_w = width_max_idx-2
#     small_h = width_max_idx-3
# elif width_max_idx-1 == length_max_idx: # length -> width 순서
#     small_h = length_max_idx-2
#     small_w = length_max_idx-3

## 제거할 땅 크기 2
small_w = (width_max_idx + 3) % 6
small_l = (length_max_idx + 3) % 6

max_area = land[width_max_idx][1] * land[length_max_idx][1]
small_area = land[small_l][1] * land[small_w][1]
print((max_area - small_area) * korean_melon)