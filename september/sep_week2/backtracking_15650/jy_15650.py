def recur(n, m, start, lst):
    if len(lst) == m:
        print(*lst)
        return

    for i in range(start, n+1):
        if i not in lst:
            recur(n, m, i+1, lst + [i])

N, M = map(int, input().split())
recur(N, M, 1, [])