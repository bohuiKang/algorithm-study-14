from collections import deque
N = int(input())
people_num = [0] + list(map(int, input().split()))
arr = [[0]] + [list(map(int, input().split()))[1::] for _ in range(N)]

# visited = [0]*(N+1) # 이걸로 만들면 1- visited 해줘서 나머지 선거구 만들면 될듯

min_val = float('inf')

def check_can(lst): # ans 가 0 으로 확인되면 연결이 안되는것
    if not lst: # 모두 다 고른 경우 나머지 집합이 공집합 되어서 문제가 됨
        return 0
    # for lst_i in lst: # 이렇게 짜면 두 덩이로 되어도 연결되어 있다고 인지해버림
    #     people = arr[lst_i]
    #     ans = 0 # ans 초기화
    #     for person in people:
    #         if person in lst:
    #             ans = 1
    #             break
    #     if ans == 0:
    #         return ans
    # return ans
    check = [lst[0]]
    q = deque([lst[0]])
    while q:
        u = q.popleft()
        for v in arr[u]:
            if v in lst and v not in check:
                q.append(v)
                check += [v]
    for lst_i in lst:
        if lst_i not in check:
            return 0
    return 1


def make_other_lst(lst): # 다른 구역 만들기
    lst_2 = []
    for i in range(1, N+1):
        if i not in lst:
            lst_2 += [i]
    return lst_2

def check_sum(lst, lst_2): # 최솟값 찾기
    global min_val
    sum_1 = sum_2 = 0
    for i in lst:
        sum_1 += people_num[i]

    for i in lst_2:
        sum_2 += people_num[i]
    val = abs(sum_1 - sum_2)
    min_val = min(min_val, val)


# 조합
def make_lst(com_lst, idx):
    ans = 0
    if idx == N+1:
        if not com_lst:
            return 0

        if check_can(com_lst) == 0:
            return 0
        com_lst2 = make_other_lst(com_lst)
        if check_can(com_lst2) == 0:
            return 0

        check_sum(com_lst, com_lst2)
        return 1


    for i in range(idx, N+1):
        ans += make_lst(com_lst+[i], i+1)
    return ans

if not make_lst([],1):
    min_val = -1
print(min_val)

