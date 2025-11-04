# import sys
#
# sys.setrecursionlimit(10000)

arr = [list(input().split()) for _ in range(5)]
result = set()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, depth):
    # 기저조건 : 6자리 수가 완성되면 set에 추가
    if len(depth) == 6:
        result.add(depth)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx, ny, depth + arr[nx][ny])


for i in range(5):
    for j in range(5):
        dfs(i, j, arr[i][j])

print(len(result))