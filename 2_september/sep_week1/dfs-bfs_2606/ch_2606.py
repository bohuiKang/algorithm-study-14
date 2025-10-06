# 양방향 간선할당 후 해당 루트부터 정점개수 카운트하는 탐색
from collections import deque
V = int(input())    # V: 정점 수
E = int(input())    # E: 간선 수
# 그래프 간선할당
graph = {}
for i in range(E):  
    u, v = map(int, input().split())
    graph.setdefault(u, []).append(v)
    graph.setdefault(v, []).append(u)

def BFS(start):
    Q = deque([start])
    visited = set([start])
    cnt = -1    # 시작정점은 카운트에서 제외하므로 -1부터 카운트
    while Q:
        node = Q.popleft()
        cnt += 1
        if node in graph:
            for i in graph[node]:
                if i not in visited:
                    visited.add(i)
                    Q.append(i)
    return cnt

print(BFS(1))