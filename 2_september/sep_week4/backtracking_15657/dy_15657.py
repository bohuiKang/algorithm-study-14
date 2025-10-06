n, m = map(int, input().split())
path = [0] * m

lst = list(map(int, input().split()))
#비내림차순을 위해 정렬
lst.sort()

def recur(cnt, idx):
    if cnt == m:
        print(*path)
        return

    for i in range(idx, n):
        path[cnt] = lst[i]
        recur(cnt + 1, i)


recur(0, 0)