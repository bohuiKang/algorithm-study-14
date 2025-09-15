N = int(input())    # N: NxN 배열의 길이
arr = [list(map(int, input())) for _ in range(N)]   # arr: NxN 2차원 배열

Dr = [0, 0, -1, 1]
Dc = [-1, 1, 0 ,0]
# 1. 무향 그래프 간선할당
graph = {}
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            u = (i, j)
            graph.setdefault(u, [])
            for p in range(4):
                Ni, Nj = i + Dr[p], j + Dc[p]
                if Ni < 0 or Ni >= N or Nj < 0 or Nj >= N:
                    continue
                if arr[Ni][Nj] == 1:
                    v = (Ni, Nj)
                    graph[u].append(v)
# 2. DFS 함수 생성(stack)
def DFS(start):
    cnt = 0
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            cnt += 1
            stack.extend(graph[node])
    return cnt
# 3. visited는 글로벌로 공유해서 다음번 DFS탐색때 건너뛰도록 하기
visited = set()
result = []
# 4. 행우선순회로 연결된 집들 탐색해서 result에 cnt를 담음
for i in range(N):
    for j in range(N):
        if (i, j) in graph and (i, j) not in visited:
            result.append(DFS((i, j)))
# 5. result를 sort해서 출력
result.sort()
print(len(result))
for cnt in result:
    print(cnt)