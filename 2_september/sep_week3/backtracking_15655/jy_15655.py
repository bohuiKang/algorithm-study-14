def recur(start, lst):
    if len(lst) == M:
        print(*lst)
        return

    for i in range(start, N):
        #start 기준으로 다음 원소 탐색, 중복 방지
        recur(i + 1, lst + [nums_lst[i]])

N, M = map(int, input().split())
#처음부터 정렬해놓기
nums_lst = sorted(list(map(int, input().split())))
recur(0, [])