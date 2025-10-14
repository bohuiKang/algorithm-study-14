n, m = map(int, input().split())
lst = list(map(int, input().split()))
# 사전순 출력을 위해 정렬
lst.sort()
path = [0]*m
result = set()

def recur(cnt):
    if cnt == m:
        #중복방지를 위해 set에 튜플로 변환하여 추가
        result.add(tuple(path))
        return
    
    for i in range(n):
        path[cnt] = lst[i]
        recur(cnt+1)

recur(0)
result = list(result)
result.sort()

for r in result:
    print(*r)