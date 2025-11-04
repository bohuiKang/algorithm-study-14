from collections import deque

def bfs(N, M):
    visited = [False] * 100001
    q = deque()
    q.append((N, 0))
    visited[N] = True

    while q:
        val, cnt = q.popleft()
        if val == M:
            return cnt

        for nxt in (val + 1, val - 1, val * 2):
            if 0 <= nxt <= 100000 and not visited[nxt]:
                visited[nxt] = True
                q.append((nxt, cnt + 1))

N, M = map(int, input().split())
print(bfs(N, M))