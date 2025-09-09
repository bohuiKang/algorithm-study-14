# 퇴사

def plan(finish, earn):
    global max_earn

    if finish > N:
        return

    for i in range(N):
        if i+1 > finish: # 일의 시작일이 끝난 날자보다 뒤일때
            plan(i + work[i][0], earn+work[i][1])
    else:
        if max_earn < earn:
            max_earn = earn
        return

N = int(input()) # N일

work = [list(map(int, input().split())) for _ in range(N)] # 일거리

max_earn = 0
plan(0, 0)
# print(work)
print(max_earn)