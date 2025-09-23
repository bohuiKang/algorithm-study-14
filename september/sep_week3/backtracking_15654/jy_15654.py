N, M = map(int, input().split())
#먼저 정렬을 해놓고 시작
n_lst = sorted(list(map(int, input().split())))
result = []

def recur(lst):
    if len(lst) == M:
        #중복 방지
        if lst not in result:
            print(*lst)
        return

    for i in range(N):
        if n_lst[i] not in lst:
            recur(lst + [n_lst[i]])

recur([])