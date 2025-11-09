dc = [0, 1, 0, -1]
dr = [1, 0, -1, 0]

def recur(cc, cr, lst):

    if len(lst) == 6:
        lst = tuple(lst)
        result.add(lst)
        return

    for i in range(4):
        nc = cc + dc[i]
        nr = cr + dr[i]

        if 0 <= nc < 5 and 0 <= nr < 5:
            recur(nc, nr, lst + [arr[nc][nr]])

arr = [list(map(int, input().split())) for _ in range(5)]
result = set()

for i in range(5):
    for j in range(5):
        recur(i, j, [arr[i][j]])

print(len(result))

# dc = [0, 1, 0, -1]
# dr = [1, 0, -1, 0]
#
# def recur(cc, cr, lst):
#
#     if len(lst) == 6:
#         result.add(lst)
#         return
#
#     for i in range(4):
#         nc = cc + dc[i]
#         nr = cr + dr[i]
#
#         if 0 <= nc < 5 and 0 <= nr < 5:
#             recur(nc, nr, lst + arr[nc][nr])
#
# arr = [input().split() for _ in range(5)]
# result = set()
#
# for i in range(5):
#     for j in range(5):
#         recur(i, j, arr[i][j])
#
# print(len(result))



