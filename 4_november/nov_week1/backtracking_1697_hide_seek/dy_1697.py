from collections import deque

# 최단 시간이니 bfs로?
def bfs(n, k):

    # (현재 위치, 걸린 시간)
    q = deque([(n, 0)])
    visited = [True] * 200001
    # 방문 표시, 방문한 곳은 방문할 필요 없기에
    visited[n] = False
    while q:
        now, hour = q.popleft()

        if now == k:
            return hour

        # 전진
        forward = now+1
        # 뒤로
        back = now-1
        # 순간이동
        tele = now*2

        # 유효성 검사 and 방문한적 없다면 행동
        if forward <= 200000 and visited[forward]:
            q.append((forward, hour+1))
            visited[forward] = False

        # 제발 인덱스 오류
        if 0 <= back <= 200000 and visited[back]:
            q.append((back, hour+1))
            visited[back] = False

        if tele <= 200000 and visited[tele]:
            q.append((tele, hour+1))
            visited[tele] = False

    return '갈수없음'

n, k = map(int, input().split())
print(bfs(n, k))