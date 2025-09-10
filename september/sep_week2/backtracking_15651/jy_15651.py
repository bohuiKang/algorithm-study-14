N, M = map(int, input().split())

def recur(n, m, lst):
    if len(lst) == m:
        print(*lst)
        return

    for i in range(1, n+1):
        recur(n, m, lst + [i])

recur(N, M, [])