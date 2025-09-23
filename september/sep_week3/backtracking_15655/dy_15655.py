n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
path = [0]*m
used = [0]*n

def recur(cnt, idx):
    if cnt == m:
        print(*path)
        return

    for i in range(idx, n):
        path[cnt] = lst[i]
        recur(cnt + 1, i + 1)

recur(0, 0)