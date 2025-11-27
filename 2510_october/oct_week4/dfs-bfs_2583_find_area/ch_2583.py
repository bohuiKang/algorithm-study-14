# 2차원 0배열에 직사각형 부분을 1로 칠한다.
# dfs 4방향 델타로 visited가 아닌 모든 배열에서 탐색시작.
def dfs(start):
    stack = [start]
    total = 0
    while stack:
        i, j = stack.pop()
        if arr[i][j] == 1:  # visited 역할
            continue
        arr[i][j] = 1
        total += 1
        if (i, j) in graph:
            nxt = graph[(i, j)]
            stack.extend(nxt)
    return total

M, N, K = map(int, input().split())     # M이 행, N이 열;;
arr = [[0] * N for _ in range(M)]
for _ in range(K):
    sc, sr, ec, er = map(int, input().split())
    # 행/열 쓰기 편하게 변환
    sr, er, ec = (M - 1) - sr, M - er, ec - 1
    # 꼭짓점도 왼쪽 위랑 오른쪽 아래로 변경
    sc, sr, ec, er = sc, er, ec, sr
    # 직사각형 색칠
    for i in range(er + 1 - sr):
        for j in range(ec + 1 - sc):
            arr[sr + i][sc + j] = 1

graph = {}
for i in range(M):
    for j in range(N):
        if arr[i][j] == 0:
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = i + dr, j + dc
                if 0 <= nr < M and 0 <= nc < N and arr[nr][nc] == 0:
                    graph.setdefault((i, j), []).append((nr, nc))

space = 0
result = []
for i in range(M):
    for j in range(N):
        if arr[i][j] == 0:
            space += 1
            result.append(dfs((i, j)))


print(space)
print(*sorted(result))