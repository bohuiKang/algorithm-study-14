a, b = map(int, input().split())

arr = [input() for _ in range(a)]

row_cnt = 0
col_cnt = 0

for i in range(a):
    row_no = 0
    for j in range(b):
        if arr[i][j] == ".":
            row_no += 1
            if row_no == b:
                row_cnt += 1

for ii in range(b):
    col_no = 0
    for jj in range(a):
        if arr[jj][ii] == ".":
            col_no += 1
            if col_no == a:
                col_cnt += 1

print(max(col_cnt, row_cnt))