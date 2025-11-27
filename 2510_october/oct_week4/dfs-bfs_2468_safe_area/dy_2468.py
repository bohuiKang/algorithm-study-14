from collections import deque

delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

# 안전한 영역의 최대 개수 계산
max_area = 0
# 비의 양 (max = 100 (높이의 최대 = 100) or 안전구역의 수가 0이 되는 순간 return, 비가 아예 안내리는 경우도 체크해야하나)
rain = 0


# 비의 양에 따라 안전구역 개수 계산 함수(비의 양을 1씩 늘려서 계산 시킬 것)
def count_safe(rain):
    visited = [[True] * n for _ in range(n)]
    safe_cnt = 0
    for r in range(n):
        for c in range(n):
            # 만약 높이가 비의 양보다 높다면 안전구역이므로 방문한 적 없다면 dfs 시작
            if lst[r][c] > rain and visited[r][c]:
                # 스택 생성 및 시작점 삽입
                stack = deque([(r, c)])
                # 구역 수 증감
                safe_cnt += 1
                # 방문 표시
                visited[r][c] = False
                # dfs
                while stack:
                    # 현재 위치 pop
                    cr, cc = stack.pop()
                    # 상하좌우 delta 탐색, 안전구역 찾기
                    for j in range(4):
                        nr = cr + delta[j][0]
                        nc = cc + delta[j][1]
                        if 0 <= nr < n and 0 <= nc < n:
                            if lst[nr][nc] > rain and visited[nr][nc]:
                                stack.append((nr, nc))
                                visited[nr][nc] = False
    return safe_cnt


for i in range(100):
    cnt = count_safe(i)
    max_area = max(max_area, cnt)
    if cnt == 0:
        break
print(max_area)
