n, m = map(int, input().split())
p = [0] * m

def recur(cnt):
    #m개 다 골랐을때
    if cnt == m:
        print(*p)
        return

    for i in range(1, n + 1):
        p[cnt] = i
        recur(cnt + 1)

recur(0)