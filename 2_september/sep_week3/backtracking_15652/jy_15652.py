N, M = map(int, input().split())

def bfs(start, lst):
    if len(lst) == M:
        print(*lst)
        return

    for i in range(start, N + 1):
        if lst:
            if i < lst[-1]:
                continue
        bfs(start, lst + [i])

bfs(1, [])