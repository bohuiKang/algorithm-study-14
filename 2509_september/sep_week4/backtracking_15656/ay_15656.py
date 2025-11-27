N, M = map(int, input().split()) # 자연수 개수, M개
nums = list(map(int, input().split())) # 주어진 자연수
nums.sort()
def rec(cnt, path):
    if cnt==M: # base case
        print(*path) # 출력
        return

    for i in range(N): # 수열 만들기
        rec(cnt+1, path+[nums[i]])


rec(0, [])