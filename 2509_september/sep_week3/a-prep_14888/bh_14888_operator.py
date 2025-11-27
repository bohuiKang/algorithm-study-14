import sys; sys.stdin = open('input.txt', 'r')

def recur(idx, num, plus, minus, multi, division):
    global min_num, max_num

    if idx == N:
        min_num = min(min_num, num)
        max_num = max(max_num, num)
        return

    if plus: # 시작이 + 연산인 재귀
        recur(idx + 1, num + arr[idx], plus - 1, minus, multi, division)
    if minus: # 시작이 - 연산인 재귀
        recur(idx + 1, num - arr[idx], plus, minus - 1, multi, division)
    if multi:
        recur(idx + 1, num * arr[idx], plus, minus, multi - 1, division)
    if division:
        if num < 0: # 음수면
            recur(idx + 1, -1 * ((num * -1) // arr[idx]), plus, minus, multi, division - 1)
        else:
            recur(idx + 1, num // arr[idx], plus, minus, multi, division - 1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    operator = list(map(int, input().split())) # + - * //

    max_num = -float('inf')
    min_num = float('inf')

    recur(1, arr[0], *operator) # 인덱스, 연산결과, 연산자 개수

    print(max_num)
    print(min_num)

# 시간복잡도 매우 복잡 => N ≤ 11일 때 10! = 3,628,800 경우라서 Python에서는 시간 초과 가능성 높음.
'''
def recur(path):
    global min_num, max_num

    if len(path) == N-1:
        result = oper(path)
        min_num = min(min_num, result)
        max_num = max(max_num, result)
        return

    for k in range(N - 1):
        if not visited[k]:
            visited[k] = 1
            recur(path + [operator[k]])
            visited[k] = 0

def oper(paths):
    copy_arr = arr.copy();

    for k in range(N - 1):
        if paths[k] == 0: # +
            copy_arr[k + 1] = copy_arr[k] + copy_arr[k + 1]
        elif paths[k] == 1: # -
            copy_arr[k + 1] = copy_arr[k] - copy_arr[k + 1]
        elif paths[k] == 2: # *
            copy_arr[k + 1] = copy_arr[k] * copy_arr[k + 1]
        else: # //
            if copy_arr[k] < 0:
                copy_arr[k + 1] = -1 * ((copy_arr[k] * -1) // copy_arr[k + 1])
            else:
                copy_arr[k + 1] = copy_arr[k] // copy_arr[k + 1]

    return copy_arr[N - 1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    operator = list(map(int, input().split())) # + - * //

    visited = [0] * len(operator)

    min_num = float('inf')
    max_num = float('-inf')

    recur([]) # 연산자 순서 path

    print(max_num)
    print(min_num)
'''

# print(-20 // 3) # -7 => -6 변경
# print(0 // 5) # 0 => 가능
# print(5 // 0) # ZeroDivisionError