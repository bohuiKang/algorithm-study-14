N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

def recur(start, path):
    if len(path) == M:
        print(*path)
        return

    prev = -1
    for i in range(start, N):
        if nums[i] == prev:
            continue
        recur(i + 1, path + [nums[i]])
        prev = nums[i]

recur(0, [])