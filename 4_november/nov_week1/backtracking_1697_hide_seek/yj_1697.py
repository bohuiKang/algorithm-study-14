from collections import deque

N, K = map(int, input().split())  # 수빈이 위치, 동생 위치
visited = [-1] * 100001

# bfs
# 초기화
Q = deque([N])
visited[N] = 0
while visited[K] == -1:  # 동생 위치가 갱신되기 전까지 bfs 돌기
    cur = Q.popleft()
    for dir in [1, -1, cur]:
        n = cur + dir
        if n < 0 or n >= 100001: continue  # 범위 밖 pass
        if visited[n] != -1: continue  # 방문했던 곳 pass
        Q.append(n)
        visited[n] = visited[cur] + 1

# 동생 따라잡으면 bfs 끝
print(visited[K])