# import sys
# sys.stdin = open("input.txt", "r")
# T = int(input())
# for tc in range(1, 1+T):
N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort() # 오름차순 정렬 사전순 정렬 위해서

def back(cnt, path):
    if cnt == M:
        print(*path)
        return
    for i in nums:
        if i in path: # 이미 사용되었으면 건너뛰기
            continue
        back(cnt+1, path+[i])

back(0,[])

