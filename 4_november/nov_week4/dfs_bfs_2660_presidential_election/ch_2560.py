from collections import deque

N = int(input())    # 전체 회원의 수

# 그래프에 친구관계 간선 할당
graph = {}
while True:
    u, v = map(int, input().split())
    if (u, v) == (-1, -1):
        break
    graph.setdefault(u, []).append(v)
    graph.setdefault(v, []).append(u)

friends_num = [0] * (N + 1)  # 친구 점수 배열

# 친구 점수 탐색할 bfs
def bfs(start):
    q = deque([start])
    dist = [-1] * (N + 1)
    dist[start] = 0
    while q:
        node = q.popleft()
        if node in graph:
            for nxt in graph[node]:
                if dist[nxt] == -1:
                    dist[nxt] = dist[node] + 1
                    q.append(nxt)
    return max(dist)

# 모든 회원의 친구 점수 탐색
for key in graph:
    friends_num[key] = bfs(key)


min_point = min(valid_num for valid_num in friends_num if valid_num != 0)
candidates = [idx for idx, v in enumerate(friends_num) if v == min_point]

print(f"{min_point} {len(candidates)}")
print(*candidates)