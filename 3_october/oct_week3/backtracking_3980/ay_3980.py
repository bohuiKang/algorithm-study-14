import sys
sys.stdin = open("3980_input.txt")
def find(i, position, sum_now): # i번째 선수, 사용된 포지션, 현재까지 합
    global max_sum
    if i == 11: # base case
        max_sum = max(max_sum, sum_now)
        return

    for j in range(11):
        if arr[i][j] == 0: # 0 에는 배정되면 안되므로
            continue
        if j in position: # 이미 선택된 포지션이면 건너뛰기
            continue
        find(i+1, position+[j], sum_now + arr[i][j])



T = int(input())

for tc in range(1, 1+T):
    arr = [list(map(int, input().split())) for _ in range(11)]
    max_sum = 0
    find(0, [], 0)

    print(max_sum)