def defdef(start, cnt, path):
    if cnt == M:
        if tuple(path) not in paths:
            print(*path)
            paths.add(tuple(path))
            return

    for i in range(start, N):
        defdef(i+1, cnt + 1, path+[arr[i]])

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))

paths = set()
defdef(0, 0, []) # 시작 개수 수열

# => set()으로 중복 검사 안해도 풀림.