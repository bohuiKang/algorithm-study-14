n, m = map(int, input().split())

used = [-1]*(n+1)
path = [-1]*m
def com(depth):
    if depth == m:
        print(*path, sep=' ')
        return
    for i in range(1, n+1):
        if used[i] == -1:
            path[depth] = i
            used[i] = 1
            com(depth+1)
            path[depth] = -1
            used[i] = -1
com(0)