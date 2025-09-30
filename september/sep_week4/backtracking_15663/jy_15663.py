N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
visited = [False] * N
result = []

def bt(lst):
    if len(lst) == M:
        result.append(tuple(lst))
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            bt(lst + [nums[i]])
            visited[i] = False

bt([])
for seq in sorted(set(result)):
    print(*seq)
