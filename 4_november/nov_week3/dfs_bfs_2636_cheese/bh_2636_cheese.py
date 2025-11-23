from collections import deque

def find_air(r, c): # 치즈를 녹이는 공기를 체크
    to_melt = set() # 공기와 맞닿은 치즈 좌표 저장
    q = deque([(r, c)])
    while q:
        sr, sc = q.popleft()
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nr = sr + dr
            nc = sc + dc
            if 0 <= nr < N and 0 <= nc < M: # 판을 벗어나지 않고
                if cheeses[nr][nc] == 0 and not visited[nr][nc]: # 공기이고 방문하지 않았으면,
                    q.append((nr, nc))
                    visited[nr][nc] = True  # 공기를 True
                elif cheeses[nr][nc] != 0: # 공기와 맞닿은 치즈일 때,
                    to_melt.add((nr, nc))
    return to_melt

def melting(cheese_list): # 공기와 맞닿은 치즈 녹이기
    for r, c in cheese_list:
        cheeses[r][c] = 0
        # visited[r][c] = True

N, M = map(int, input().split())
cheeses = [list(map(int, input().split())) for _ in range(N)]

left_cheese = 0
melt_time = 0

while True:
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True
    melt_cheese = find_air(0,0) # 공기 체크

    if not melt_cheese: # 녹일 치즈가 없으면 break
        break

    # 녹일 치즈 개수 저장
    left_cheese = len(melt_cheese)
    melting(melt_cheese) # 치즈 녹이기
    melt_time += 1

print(melt_time)
print(left_cheese)
