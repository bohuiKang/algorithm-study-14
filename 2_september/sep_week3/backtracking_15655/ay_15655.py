# import sys
# sys.stdin = open("input.txt", "r")
# T = int(input())
# for tc in range(1, 1+T):
N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort() # 오름차순 정렬 - 사전 순 증가 배치 위해

def back(cnt, path, idx):
    if cnt == M: # base case
        print(*path)
        return

    if idx == N: # idx 초과 이므로 더이상 진행 못하게 막기
        return

    for i in range(idx, N):
        back(cnt+1, path+[nums[i]], i+1)

back(0, [], 0)