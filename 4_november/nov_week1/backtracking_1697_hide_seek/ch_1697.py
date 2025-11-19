# 1. 현재좌표 -1
# 2. 현재좌표 +1
# 3. 현재좌표 *2
# 기저조건 : 동생의 좌표와 만났을때

from collections import deque

N, K = map(int, input().split())
visited = [False] * 100001

def bfs(start):
    q = deque([(start, 0)])  # (현재좌표, 시간)
    visited[start] = True

    while q:
        pos, time = q.popleft()

        # 기저조건: 동생과 만났을 때
        if pos == K:
            return time

        # 세 가지 이동 경우의 수
        for next_pos in (pos - 1, pos + 1, pos * 2):
            if 0 <= next_pos <= 100000 and not visited[next_pos]:
                visited[next_pos] = True
                q.append((next_pos, time + 1))

print(bfs(N))