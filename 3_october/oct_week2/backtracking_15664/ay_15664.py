N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
def rec(cnt, idx, path):
    if cnt == M:
        print(*path)
        return

    visited = []
    for i in range(idx, N):
        if nums[i] in visited:
            continue
        rec(cnt+1, i+1, path+[nums[i]])
        visited += [nums[i]]

rec(0, 0, [])