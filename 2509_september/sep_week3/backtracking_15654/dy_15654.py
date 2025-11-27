n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
path = [0]*m
used = [0]*n

def recur(cnt, idx):
    if cnt == m:
        print(*path)
        return

    for i in range(n):
        if used[i] == 1:
            continue
        path[idx] = lst[i]
        used[i] = 1
        recur(cnt+1, idx+1)
        used[i] = 0

recur(0, 0)