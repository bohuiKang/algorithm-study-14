N = int(input())
arr = list(map(int, input().split()))   # arr: 수의 배열
op = ['+', '-', '*', '/']
num_op = list(map(int, input().split()))    # num_op: 연산자들의 수
op_list = []    # op_list: 보유한 연산자들을 개수만큼 갖고있는 배열
for i in range(4):
    op_list.extend(op[i] * num_op[i])

max_v = float('-inf')
min_v = float('inf')
visited = [0] * (N-1)

def recur(depth, total):
    global max_v, min_v

    if depth == N-1:  # N-1개의 연산자 사용했으면 종료
        max_v = max(max_v, total)
        min_v = min(min_v, total)
        return


    for i in range(N-1):
        if visited[i]:
            continue

        visited[i] = 1
        next_num = arr[depth+1]  # next_num: 다음 수
         # 연산자에 따라 4가지 경우의 수
        if op_list[i] == '+':
            recur(depth+1, total + next_num)
        elif op_list[i] == '-':
            recur(depth+1, total - next_num)
        elif op_list[i] == '*':
            recur(depth+1, total * next_num)
        elif op_list[i] == '/':
            # 음수 나눗셈 처리
            if total < 0:
                recur(depth+1, -(-total // next_num))
            else:
                recur(depth+1, total // next_num)
        visited[i] = 0

recur(0, arr[0])
print(f"{max_v}")
print(f"{min_v}")