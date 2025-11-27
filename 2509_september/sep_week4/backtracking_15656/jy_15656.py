def bt(lst):

    if len(lst) == m:
        print(*lst)
        return

    for i in range(n):
        bt(lst + [nums[i]])

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
bt([])