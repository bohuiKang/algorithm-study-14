def defdef(cnt, path):
    if cnt == M:
        if tuple(path) not in paths:
            print(*path)
            paths.add(tuple(path))
        return

    for i in range(N):
        defdef(cnt + 1, path+[arr[i]])

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))

paths = set()
defdef(0, []) # 개수 수열

