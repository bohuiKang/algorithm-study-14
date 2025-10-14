def recur(depth):
    global result

    if depth == M:
        r = tuple(result)
        if r not in used:
            print(*r)
            used.add(r)
        return

    for i in range(N):
        result.append(nums[i])
        recur(depth + 1)
        result.pop()

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
result = []
used = set()

recur(0)