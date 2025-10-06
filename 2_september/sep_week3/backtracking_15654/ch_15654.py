N, M = map(int, input().split())
num = list(map(int, input().split()))   # num: 숫자들 리스트
visited = set()
result = []
def recur(depth, path):
    if depth == M:
        result.append(path)
        return
    for i in range(N):
        if i in visited:
            continue
        visited.add(i)
        recur(depth + 1, path + [num[i]])
        visited.remove(i)
recur(0, [])
for path in sorted(result):
    print(*path)