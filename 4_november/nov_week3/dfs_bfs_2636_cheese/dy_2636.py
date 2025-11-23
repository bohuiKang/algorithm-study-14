from collections import deque
delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]

n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]

# 한시간동안 치즈 녹이기 = dfs()
# 빈 공간과 맞닿아 있는 치즈들 녹이기
# 가장자리는 모두 비어있으니 0,0에 dfs 시작
# 0,0에서 dfs, 상하좌우 탐색
# 0이 있다면 stack에 push, 1이라면 녹이기
def dfs():
    s = deque([(0,0)])
    visited = [[True] * m for _ in range(n)]
    visited[0][0] = False
    # 해당 dfs에서 녹인 치즈의 수
    cnt = 0
    while s:
        r, c = s.pop()
        # 상하좌우 탐색
        for i in range(4):
            nr = r + delta[i][0]
            nc = c + delta[i][1]
            if 0<=nr<n and 0<=nc<m and visited[nr][nc]:
                if lst[nr][nc] == 1:
                    # 방문 표시
                    visited[nr][nc] = False
                    # 녹이기
                    lst[nr][nc] = 0
                    cnt += 1
                elif lst[nr][nc] == 0:
                    # 방문 표시
                    visited[nr][nc] = False
                    # 스택에 넣기
                    s.append((nr, nc))
    # 해당 턴에 녹인 치즈 수 반환
    return cnt

# 걸린 시간
hour = 0
# 직전 턴에 녹인 치즈 수
prev_num = 0

# 다 녹일때까지 반복
while True:
    # 한시간 동안 치즈 녹이기
    num = dfs()
    # 만약 녹인 치즈의 수가 0이라면 다 녹은 상태이므로
    if num == 0:
        # 시간과 직전에 녹인 치즈의 수 출력 후 종료
        print(hour)
        print(prev_num)
        break
    else:
        # 직전 치즈의 수, 시간 갱신
        prev_num = num
        hour += 1
