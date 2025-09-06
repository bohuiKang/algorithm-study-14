def virus_affected():

    while q:
        curr = q.pop(0)
        for c in computer[curr]:
            if not visited[c]:
                q.append(c)
                visited[c] = True

n = int(input())
e = int(input())

computer = [[] for _ in range(n+1)]
cp_lst = [list(map(int, input().split())) for _ in range(e)]
visited = [False] * (n+1)
visited[1] = True
q = [1]

for c in cp_lst:
    computer[c[0]].append(c[1])
    computer[c[1]].append(c[0])

virus_affected()
result_cnt = 0

for i in range(n+1):
    if i != 1 and visited[i]:
        result_cnt += 1

print(result_cnt)