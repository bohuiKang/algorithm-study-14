from collections import deque

dc = [-1, -2, -2, -1, 1, 2, 2, 1]
dr = [-2, -1, 1, 2, 2, 1, -1, -2]

def bt(c, r):
    q = deque()
    q.append((c, r))

    while q:
        cc, cr = q.popleft()

        if cc == wc and cr == wr:
            break

        for dir in range(8):
            nc = cc + dc[dir]
            nr = cr + dr[dir]

            if 0 <= nc < I and 0 <= nr < I and arr[nc][nr] == 0:
                arr[nc][nr] = arr[cc][cr] + 1
                q.append((nc, nr))

    return arr[wc][wr]

T = int(input())
for _ in range(T):
    I = int(input())
    fc, fr = map(int, input().split())
    wc, wr = map(int, input().split())

    arr = [[0]*I for _ in range(I)]

    if fc == wc and wc == wr:
        print(0)
    else:
        print(bt(fc, fr))