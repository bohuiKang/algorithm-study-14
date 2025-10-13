def defdef(start, cnt, path):
    if cnt == M:
        if tuple(path) not in paths:
            print(*path)
            paths.add(tuple(path))
        return

    for i in range(start, N):
        defdef(i, cnt + 1, path+[arr[i]])
        defdef(i+1, cnt + 1, path+[arr[i]])

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))

paths = set()
defdef(0, 0, []) # 개수 수열

