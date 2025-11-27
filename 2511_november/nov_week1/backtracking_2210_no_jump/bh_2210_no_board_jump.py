def recur(sr, sc, path):

    if len(path) == 6:
        six_num.add(tuple(path))
        return

    for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nr = sr + dr
        nc = sc + dc
        if 0 <= nr < 5 and 0 <= nc < 5:
            recur(nr, nc, path+[arr[nr][nc]])


arr = [list(map(int, input().split())) for _ in range(5)]
six_num = set() # 중복을 제거할 set

for r in range(5): # 0-4
    for c in range(5): # 0-4
        recur(r, c, [arr[r][c]])

print(len(six_num))
