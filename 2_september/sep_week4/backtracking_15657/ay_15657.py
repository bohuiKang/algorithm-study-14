N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

def rec(cnt, path, idx):
    if cnt == M:
        print(*path)
        return

    for i in range(idx, N):
        rec(cnt+1, path+[nums[i]], i)

rec(0, [], 0)

