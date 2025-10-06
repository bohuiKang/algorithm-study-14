N, M = map(int, input().split())
path = []
def permu(cnt,idx):

    if cnt == M: #M개 만큼 새면 RETURN
        print(*path)
        return

    for i in range(idx,N+1):
        path.append(i)
        permu(cnt+1,i+1)
        path.pop()

permu(0,1)

