N = int(input())

lv_scor = [int(input()) for _ in range(N)]

idx = N-1
cnt = 0
while idx > 0:
    if lv_scor[idx] <= lv_scor[idx-1]:
        lv_scor[idx - 1] -= 1
        cnt += 1
    else:
        idx -= 1

print(cnt)