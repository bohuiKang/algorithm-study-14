n, m = map(int, input().split())
path = [0] * m

lst = list(map(int, input().split()))
# 사전순 출력을 위해 정렬
lst.sort()


def recur(cnt):
    if cnt == m:
        print(*path)
        return

    for i in range(n):
        path[cnt] = lst[i]
        recur(cnt+1)


recur(0)