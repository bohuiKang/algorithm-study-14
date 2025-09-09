N = int(input())
T = [0]*(N+1)
P = [0]*(N+1)
for i in range(1,N+1):
    T[i], P[i] = map(int, input().split())


max_sum = 0
def dfs(idx, p_sum): # idx는 앞에 상담일 끝난 다음날
    global max_sum
    if idx >= N+1:
        max_sum = max(max_sum, p_sum)
        return

    for i in range(idx, N+1):
        if i+T[i] <= N+1:
            dfs(i+T[i], p_sum+P[i]) # i+T[i] 하면 상담 끝난 그 다음날 idx가 들어감
        else:
            dfs(i+T[i], p_sum) #  퇴직날 이후로 idx가 잡히게 되면 수익 더해주면 안됨

dfs(1,0)
print(max_sum)