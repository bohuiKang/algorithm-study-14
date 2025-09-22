# N, M = map(int, input().split())
# n_lst = sorted(list(map(int, input().split()))) #처음부터 정렬을 해놓고 시작
#
# def recur(lst):
#     if len(lst) == M:
#         if lst not in result:
#             print(*lst)
#         return
#
#     for i in range(N):
#         if n_lst[i] not in lst: #중복 방지
#             recur(lst + [n_lst[i]])
#
# recur([])
N, M = map(int, input().split())
n_lst = sorted(list(map(int, input().split())))

used = [False] * N
seq = []

def recur(depth):
    if depth == M:
        print(*seq)
        return
    for i in range(N):
        if not used[i]:
            used[i] = True
            seq.append(n_lst[i])
            recur(depth + 1)
            seq.pop()
            used[i] = False

recur(0)
