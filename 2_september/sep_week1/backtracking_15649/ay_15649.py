N, M = map(int, input().split()) # N까지 자연수 M수열 길이
path=[]
def backtrack(cnt):

    if cnt == M: # 수열 길이 도달시 출력
        print(*path)
        return

    for i in range(1,N+1): # 수열이라서 1부터 N까지 다 돌아가면서 첨가하면 됨
        if i not in path: # 중복 된것은 pass
            path.append(i)
            backtrack(cnt+1)
            path.pop()

backtrack(0)