def bt(start, lst):
    if len(lst) == m:
        print(*lst)
        return

    for i in range(start, len(nums)):
        bt(i, lst + [nums[i]])

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
bt(0, [])
