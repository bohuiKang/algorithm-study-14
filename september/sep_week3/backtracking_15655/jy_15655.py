# def recur(start, lst):
#     if len(lst) == M:
#         print(*lst)
#         return
#
#     for i in range(start, N):
#         if nums_lst[i] not in lst:
#             recur(start + 1, lst + [nums_lst[i]])
#
# N, M = map(int, input().split())
# nums_lst = sorted(list(map(int, input().split())))
# recur(0, [])