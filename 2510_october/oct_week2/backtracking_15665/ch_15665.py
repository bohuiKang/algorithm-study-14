N, M = map(int, input().split())
arr = list(map(int, input().split()))
result = set()

def recur(depth, path):
    if depth == M:
        result.add(tuple(path))
        return

    for i in range(N):
        recur(depth + 1, path + [arr[i]])

recur(0, [])
result = list(result)
result.sort()
for p in result:
    print(*p)