N, M = map(int, input().split())
path = []
def per(cnt, lst):
    if cnt == M:
        print(*lst)
        return

    for i in range(1, N+1):
        path.append(i)
        per(cnt+1)
        path.pop() #1900ms

    # for i in range(1, N+1):
    #     per(cnt+1, lst+[i]) # 1900ms

per(0,path)
