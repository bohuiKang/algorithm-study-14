from itertools import permutations

N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]

for p in permutations(arr, M):
    print(*p)

#---------
def recur(n, m, lst):
    if len(lst) == m:
        print(*lst)
        return

    for i in range(1, n+1):
        if i not in lst:
            recur(n, m, lst + [i])

N, M = map(int, input().split())
recur(N, M, [])