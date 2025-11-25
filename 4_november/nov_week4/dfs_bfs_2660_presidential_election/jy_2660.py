'''
점수: 다른 모든 회원들에게 연락하기 위해 거쳐야 하는 최대 단계 (촌수)
나랑 상대방이 친구 -> 거리 1 -> 점수 1
나랑 상대방이 친구의 친구 -> 거리 2 -> 점수 2
나랑 상대방이 친구의 친구의 친구 -> 거리 3 -> 점수 3

어떤 두 회원이 친구 사이인 동시에 친구의 친구 사이라면 두 사람은 친구 사이다
-> 최단 거리를 인정한다는 소리

회장의 조건은 점수가 가장 적은 사람, 모임의 중심에 있는 사람
인싸일수록 점수가 낮다 ... 잔소리 좀 그만해라 진짜 아 짜증나
모든 회원의 점수를 구한 뒤 점수가 최소인 사람이 회장 후보
'''

from collections import deque

N = int(input())  # 회원 수 입력받기
graph = [[] for _ in range(N + 1)]

while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:  # 입력 종료 조건
        break
    graph[a].append(b)
    graph[b].append(a)


# 2. BFS 함수 정의
def bfs(start_v):
    visited = [-1] * (N + 1)  # 방문 여부 및 거리 저장 (-1은 미방문)
    visited[start_v] = 0  # 나 자신은 거리 0
    queue = deque([start_v])

    local_max_dist = 0  # 현재 회원의 점수(가장 먼 거리)

    while queue:
        cur = queue.popleft()

        for nxt in graph[cur]:
            if visited[nxt] == -1:  # 아직 방문하지 않은 친구라면
                visited[nxt] = visited[cur] + 1  # 거리를 1 늘려서 저장
                queue.append(nxt)
                local_max_dist = max(local_max_dist, visited[nxt])  # 최대 거리 갱신

    return local_max_dist


# 3. 모든 회원에 대해 점수 계산
scores = []
min_score = float('inf')  # 최소 점수(회장 점수)를 찾기 위한 변수

for i in range(1, N + 1):
    score = bfs(i)
    scores.append(score)
    if score < min_score:
        min_score = score

# 4. 회장 후보 찾기 (점수가 min_score인 사람들)
candidates = []
for i in range(N):
    # i는 0부터 시작하므로, 회원 번호는 i+1
    if scores[i] == min_score:
        candidates.append(i + 1)

# 5. 결과 출력
print(f"{min_score} {len(candidates)}")
print(*candidates)