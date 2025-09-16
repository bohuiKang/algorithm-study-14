n, m = map(int, input().split())
p = [0] * m

def recur(cnt, start):
    #m개 다 골랐을때
    if cnt == m:
        print(*p)
        return

    for i in range(start, n + 1):
        p[cnt] = i
        recur(cnt + 1, i + 1)

recur(0, 1)
