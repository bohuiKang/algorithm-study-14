import sys
sys.stdin = open("2606_input.txt", "r")

V = int(input())  # 정점 수
E = int(input())  # 간선 수

edges = [[] for _ in range(V + 1)]  # 각 인덱스 번호 -> 정점 번호
visited = [0] * (V + 1)  # 방문 확인

for i in range(E):  # 인접 리스트 저장, 무향
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)

def dfs(v): # v= 방문할 정점 번호
    visited[v] = 1
    for w in edges[v]:
        if not visited[w]:  # 방문 한적이 없으면 0이라서
            dfs(w)

dfs(1)
cnt = -1 # 1번 제외라서
for i in visited:
    if i:
        cnt += 1

# cnt = 0
# for i in range(2, V+1): # 이렇게 해도 될듯?
#     if visited[i]:
#         cnt += 1

print(cnt)