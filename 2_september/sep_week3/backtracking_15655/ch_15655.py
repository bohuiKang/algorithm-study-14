N, M = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
visited = set()

def recur(depth, path):
    for i in range(depth - 1):
        if path[i] >= path[i + 1]:
            return
    
    if depth == M:
        print(*path)
        return
    
    for i in range(N):
        if i in visited:
            continue
        visited.add(i)
        recur(depth + 1, path + [num[i]])
        visited.remove(i)

recur(0, [])