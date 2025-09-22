def recur(idx, num, add, sub, mul, div):
    global max_result, min_result

    if idx == N:
        max_result = max(max_result, num)
        min_result = min(min_result, num)

    if add:
        recur(idx + 1, num + num_lst[idx], add - 1, sub, mul, div)
    if sub:
        recur(idx + 1, num - num_lst[idx], add, sub - 1, mul, div)
    if mul:
        recur(idx + 1, num * num_lst[idx], add, sub, mul - 1, div)
    if div:
        recur(idx + 1, int(num / num_lst[idx]), add, sub, mul, div - 1)


N = int(input())
num_lst = list(map(int, input().split()))
ope_list = list(map(int, input().split()))
max_result = -float('inf')
min_result = float('inf')

recur(1, num_lst[0], ope_list[0], ope_list[1], ope_list[2], ope_list[3])
print(max_result)
print(min_result)