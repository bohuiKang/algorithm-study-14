N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

def rec(cnt, idxs, path):
    if cnt == M:
        print(*path)
        return

    visited = []
    for i in range(N):
        if nums[i] in visited:
            continue
        if i in idxs:
            continue
        rec(cnt+1, idxs + [i], path+[nums[i]])
        visited += [nums[i]]

rec(0, [], [])
