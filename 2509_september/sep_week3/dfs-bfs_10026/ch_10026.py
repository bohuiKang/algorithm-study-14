# 상하좌우 같은 색이면 같은 구역
# 적록색약은 R, G가 같은 색
N = int(input())
arr = [list(input().strip()) for _ in range(N)]
Dr, Dc = [0, 0, 1, -1], [1, -1, 0, 0]

def DFS_1(start):
    stack = [start]
    while stack:
        r, c = stack.pop()
        if not visited[r][c]:
            visited[r][c] = 1
            for d in range(4):
                Nr = r + Dr[d]
                Nc = c + Dc[d]
                if Nr < 0 or Nr >= N or Nc < 0 or Nc >= N:
                    continue
                if arr[r][c] == arr[Nr][Nc]:    # 인접정점이 색이 같으면 같은 구역
                    stack.append((Nr, Nc))

def DFS_2(start):
    stack = [start]
    while stack:
        r, c = stack.pop()
        if not visited[r][c]:
            visited[r][c] = 1
            for d in range(4):
                Nr = r + Dr[d]
                Nc = c + Dc[d]
                if Nr < 0 or Nr >= N or Nc < 0 or Nc >= N:
                    continue
                if arr[r][c] in ['R', 'G'] and arr[Nr][Nc] in ['R', 'G']:   # 적녹일때
                    stack.append((Nr, Nc))
                elif arr[r][c] == arr[Nr][Nc]:  # 파란색일때
                    stack.append((Nr, Nc))

# 일반인 행우선 순회
visited = [[0] * N for _ in range(N)]
result_1 = 0
for i in range(N):
    for j in range(N):
        if visited[i][j]:
            continue
        DFS_1((i, j))
        result_1 += 1

# 적록색약 행우선 순회
visited = [[0] * N for _ in range(N)]
result_2 = 0
for i in range(N):
    for j in range(N):
        if visited[i][j]:
            continue
        DFS_2((i, j))
        result_2 += 1

print(f"{result_1} {result_2}")