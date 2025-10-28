from collections import deque

dc = [0, 1, 0, -1]
dr = [1, 0, -1, 0]

def bfs(r):
    # 임시 arr를 만들어줌 -> 가라앉는 지역과 방문지역을 표시해둘 예정
    temp = [[0] * N for _ in range(N)]
    # 안전지대 지역 cnt
    cnt = 0

    # r(비의 양)보다 arr이 낮다면 같은 위치의 temp를 -1로 처리 (가라앉았다는 뜻)
    for i in range(N):
        for j in range(N):
            if arr[i][j] < r:
                temp[i][j] = -1

    # 가라앉은 곳을 다 표시한 뒤 0인 == 가라앉지 않은 구역을 확인하면 주변 인접 안전지대 탐색
    for i in range(N):
        for j in range(N):
            if temp[i][j] == 0:
                find_safe(i, j, temp)
                # 한 번 돌면 안전지대 + 1
                cnt += 1

    # 안전지대의 개수 반환
    return cnt

def find_safe(sc, sr, temp_arr):
    q = deque()
    q.append([sc, sr])

    while q:
        cc, cr = q.popleft()
        for i in range(4):
            nc = cc + dc[i]
            nr = cr + dr[i]
            if 0 <= nc < N and 0 <= nr < N and temp_arr[nc][nr] == 0:
                q.append([nc, nr])
                # temp에 방문처리
                temp_arr[nc][nr] = -1

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# 올 수 있는 비의 양들을 저장해둘 set
rains = set()
max_count = -float('inf')

# rains에 비를 저장해둠
for a in arr:
    for char in a:
        rains.add(char)

# 올 수 있는 비의 양에 대해 안전구역을 확인해보기
for rain in rains:
    # result = bfs로 나올 수 있는 안전구역의 개수
    result = bfs(rain)
    max_count = max(max_count, result)

print(max_count)