# import sys
# sys.stdin = open("input.txt", "r")
# T = int(input())
# for tc in range(1, 1+T):
N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort() # 오름차순 정렬

def back(cnt, path, used):
    if cnt == M:
        print(*path)
        return
    for i in nums:
        if i in used:
            continue
        back(cnt+1, path+[i], used+[i])

back(0,[],[])

