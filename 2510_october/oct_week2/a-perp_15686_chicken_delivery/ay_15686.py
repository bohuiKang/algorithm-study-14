# from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# dr = [0, 1, 0, -1]
# dc = [1, 0, -1, 0]


def count_ch():  # 치킨집 개수 , 집 개수 세기
    chicken_list = []
    house_list = []
    ch_cnt = 0
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 2:
                chicken_list.append((r,c))
                ch_cnt += 1
            elif arr[r][c] == 1:
                house_list.append((r,c))

    return chicken_list, ch_cnt, house_list # 각각의 좌표를 리스트로 만들어서 return

def min_length(chicken_path): # 주어진 리스트의 최솟값 찾기
    total_length = 0
    for house in house_list:
        new_len = [0] * M # 한 집당- 치킨집들의 거리 리스트를 만듬
        for i in range(M):
            new_len[i] = abs(house[0]-chicken_path[i][0]) + abs(house[1]-chicken_path[i][1])
        total_length += min(new_len) # 제일 작은 값만 전체 길이에 더함

    return total_length


min_val = float("inf")
def left_chicken(ch_cnt, cnt, idx, path): # 치킨집 리스트 만들기
    global min_val
    if ch_cnt == M: # 이미 개수 같으면 재귀 돌지 않고 바로 빠져나옴 -> 근데 이걸 함수 밖에 빼서 확인하고 함수를 안돌려도 될듯
        min_val = min_length(chicken_list)
        return

    if cnt == M:
        length = min_length(path) #
        min_val = min(length, min_val)
        return

    for i in range(idx, ch_cnt): # 최소 치킨집 개수에 맞춰 치킨집 위치 리스트 구성
        left_chicken(ch_cnt, cnt+1, i+1, path+[chicken_list[i]])








chicken_list, ch_cnt, house_list = count_ch()
left_chicken(ch_cnt, 0, 0, [])

print(min_val)