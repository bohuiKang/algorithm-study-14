N, M = map(int, input().split())
def recur(depth, path):
    if depth == M:
        print(*path)
        return
    for i in range(1, N + 1):
        recur(depth + 1, path + str(i))
recur(0, '')