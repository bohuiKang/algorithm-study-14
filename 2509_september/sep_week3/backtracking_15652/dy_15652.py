#1과 N까지 자연수 중에서 M개를 고른 수열
#중복 허용
#고른 수열은 비내림차순
#A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK

n, m = map(int, input().split())
path = [0]*m

def recur(cnt, idx):

    if cnt == m:
        print(*path)
        return

    for i in range(1, n+1):
        path[idx] = i
        if idx > 0:
            if path[idx] < path[idx-1]:
                continue
        recur(cnt+1, idx+1)

recur(0, 0)