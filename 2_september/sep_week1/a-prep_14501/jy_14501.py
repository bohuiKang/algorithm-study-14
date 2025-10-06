def find_max(curr_profit, curr_idx):
    global max_profit

    #현재 위치가 주어진 범위를 초과할 경우 return
    if curr_idx > N:
        return

    if curr_idx == N:
        max_profit = max(max_profit, curr_profit)
        return

    #1) 해당 날짜의 상담을 진행하는 경우
    find_max(curr_profit + reservation[curr_idx][1], curr_idx + reservation[curr_idx][0])

    #2) 해당 날짜의 상담을 진행하지 않고 넘어가는 경우
    find_max(curr_profit, curr_idx+1)

N = int(input())
reservation = [list(map(int, input().split())) for _ in range(N)]
max_profit = -float('inf')

find_max(0, 0)
print(max_profit)