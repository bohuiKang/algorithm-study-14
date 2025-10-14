N, M = map(int, input().split())
arr = list(map(int, input().split()))
result = set()

def recur(depth, path):
    for i in range(len(path) - 1):
        if path[i] > path[i + 1]:
            return

    if depth == M:
        result.add(tuple(sorted(path)))
        return

    for i in range(N):
        recur(depth + 1, path + [arr[i]])


recur(0, [])
result = list(result)
result.sort()
for p in result:
    print(*p)