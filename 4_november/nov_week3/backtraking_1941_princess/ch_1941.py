# dfs로 인접한 S와 Y를 선택해 총 7개 선택
# Y가 4개 이상이 되면 리턴
from collections import deque

arr = [list(input().strip()) for _ in range(5)]

# 0 ~ 24 번째 위치를 (r, c)로 미리 저장
positions = [(r, c) for r in range(5) for c in range(5)]

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

ans = 0


# 뽑힌 7칸이 서로 인접한지 확인
def is_connected(selected):
    q = deque()
    visited = set()

    q.append(selected[0])
    visited.add(selected[0])
    selected_set = set(selected)

    while q:
        r, c = q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < 5 and 0 <= nc < 5:
                if (nr, nc) in selected_set and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    q.append((nr, nc))

    return len(visited) == 7


def dfs(idx, selected, s_cnt, y_cnt):
    global ans

    # Y가 4명 이상이면 가지치기
    if y_cnt >= 4:
        return

    # 기저조건: 7명 다 뽑은 경우
    if len(selected) == 7:
        if s_cnt >= 4 and is_connected(selected):
            ans += 1
        return

    # 인덱스를 다 썼으면 종료
    if idx == 25:
        return

    # 남은 칸 수로 7명을 못 채우면 가지치기
    remaining = 25 - idx
    need = 7 - len(selected)
    if remaining < need:
        return

    r, c = positions[idx]

    # 현재 칸을 선택하는 경우
    if arr[r][c] == 'S':
        dfs(idx + 1, selected + [(r, c)], s_cnt + 1, y_cnt)
    else:
        dfs(idx + 1, selected + [(r, c)], s_cnt, y_cnt + 1)

    # 현재 칸을 선택하지 않는 경우
    dfs(idx + 1, selected, s_cnt, y_cnt)


dfs(0, [], 0, 0)
print(ans)