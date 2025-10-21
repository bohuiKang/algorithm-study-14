# 재귀함수로 그래프를 탐색한다. 한번 정점을 선택할때마다 할일
# 1. 남은 정점들이 모두 연결되어있는지 bfs를 이용해 확인(visited) -> 연결안되어있으면 return
# 2. 남은 정점들과 현재 탐색한 정점들의 가중치 차이를 min_v와 갱신
# 3. min_v 보다 가중치 차이가 커지면 가지치기 가능
from collections import deque
N = int(input())
weights = list(map(int, input().split()))   # 각 지점들의 가중치(인구 수)
weights = [0] + weights     # 1번 인덱스부터 사용

# 그래프 간선할당
graph = {}
for i in range(1, N + 1):
    v_list = list(map(int, input().split()))
    v_list.pop(0)   # 인접구역 수 필요없음
    graph.setdefault(i, []).extend(v_list)

# 재귀함수 구현
min_v = float('inf')
all_weights = sum(weights)
r_visited = [0] * (N + 1)       # recur 에서 사용할 visited
def recur(node, selected, weight):
    global min_v
    weight += weights[node]
    if len(selected) > 0:
        other_group = [i for i in range(1, N + 1) if i not in selected]
        if not other_group:
            return
        # 각 그룹의 연결 확인 후 최솟값 갱신
        if bfs(selected[0], selected) and bfs(other_group[0], other_group):
            diff = abs((all_weights - weight) - weight)
            min_v = min(min_v, diff)
    for nxt in range(node + 1, N + 1):
        if r_visited[nxt]:
            continue
        r_visited[nxt] = 1
        recur(nxt, selected + [nxt], weight)
        r_visited[nxt] = 0

# 반대편 연결 확인용 bfs 구현
def bfs(start, group):
    q = deque([start])
    visited = set([start])
    while q:
        node = q.popleft()
        for nxt in graph[node]:
            if nxt in group and nxt not in visited:
                visited.add(nxt)
                q.append(nxt)
    return len(visited) == len(set(group))  # 연결 유무를 boolean 타입으로 반환

for i in range(1, N + 1):
    r_visited[i] = 1
    recur(i, [i], 0)
    r_visited[i] = 0

print(min_v if min_v != float('inf') else -1)